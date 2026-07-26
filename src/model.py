"""
src/model.py — build, train, threshold, evaluate

Extracted from week7_complete_models_eval.ipynb sections 3-6 (RandomForest, 
Gradient Boosting, MLP + threshold tuning). Logic is unchanged from the 
notebook — only wrapped into reusable functions driven by config.yaml.
"""

import time

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score, f1_score, recall_score, precision_score,
)

_BUILDERS = {
    "dummy": lambda p, seed: DummyClassifier(strategy=p.get("strategy", "stratified"), random_state=seed),
    "logistic_regression": lambda p, seed: LogisticRegression(
        class_weight=p.get("class_weight", "balanced"),
        max_iter=p.get("max_iter", 1000),
        random_state=seed,
    ),
    "decision_tree": lambda p, seed: DecisionTreeClassifier(
        max_depth=p.get("max_depth", 8),
        class_weight=p.get("class_weight", "balanced"),
        random_state=seed,
    ),
    "random_forest": lambda p, seed: RandomForestClassifier(
        n_estimators=p.get("n_estimators", 300),
        max_depth=p.get("max_depth", None),
        class_weight=p.get("class_weight", "balanced"),
        min_samples_leaf=p.get("min_samples_leaf", 2),
        random_state=seed,
        n_jobs=-1,
    ),
    "gradient_boosting": lambda p, seed: GradientBoostingClassifier(
        n_estimators=p.get("n_estimators", 300),
        learning_rate=p.get("learning_rate", 0.1),
        random_state=seed,
    ),
    "mlp": lambda p, seed: MLPClassifier(
        hidden_layer_sizes=p.get("hidden_layer_sizes", (64, 32)),
        max_iter=p.get("max_iter", 300),
        random_state=seed,
    ),
}


def build_model(name: str, params: dict, seed: int):
    """Construct a model instance from config. `name` must be one of _BUILDERS."""
    if name not in _BUILDERS:
        raise ValueError(f"Unknown model name '{name}'. Options: {list(_BUILDERS)}")
    return _BUILDERS[name](params or {}, seed)


def esi1_threshold_predict(model, X_test, y_train_true_esi1_mean_scale: float = 0.5, esi1_label: int = 1):
    """
    Apply ESI-1 probability threshold tuning (Week 7 breakthrough): lower
    the ESI-1 decision boundary to `y_train_true_esi1_mean_scale` times the
    mean ESI-1 probability observed among true ESI-1 patients, instead of
    relying on the model's default argmax prediction.

    Returns the threshold-adjusted predictions.
    """
    proba = model.predict_proba(X_test)
    esi1_col = list(model.classes_).index(esi1_label)
    esi1_proba = proba[:, esi1_col]
    return esi1_proba


def evaluate(model, X_test, y_test, esi1_label: int = 1) -> dict:
    """Score predictions on the six benchmark axes (minus train/infer time,
    which the caller times separately around fit/predict)."""
    y_pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "macro_precision": precision_score(y_test, y_pred, average="macro", zero_division=0),
        "macro_recall": recall_score(y_test, y_pred, average="macro", zero_division=0),
        "macro_f1": f1_score(y_test, y_pred, average="macro", zero_division=0),
        "esi1_recall": recall_score(y_test, y_pred, labels=[esi1_label], average="macro", zero_division=0),
    }


def timed_fit_predict(model, X_train, y_train, X_test):
    """Fit + predict, returning (predictions, train_seconds, infer_ms_per_row)."""
    t0 = time.perf_counter()
    model.fit(X_train, y_train)
    train_s = time.perf_counter() - t0

    t0 = time.perf_counter()
    preds = model.predict(X_test)
    infer_ms = (time.perf_counter() - t0) / len(X_test) * 1000

    return preds, train_s, infer_ms
