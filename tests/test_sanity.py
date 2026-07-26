"""
tests/test_sanity.py

Two sanity checks. These do NOT prove the code is
perfect — they prove it breaks LOUDLY if cleaning or training silently goes wrong.

Run: pytest tests/test_sanity.py
"""

import sys
import os
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data import clean, VITALS, TARGET
from src.model import build_model


def _make_fake_raw(n=60, seed=27):
    """Build a tiny synthetic raw frame with the same columns clean() expects."""
    rng = np.random.default_rng(seed)
    data = {
        "esi": rng.integers(1, 6, size=n).astype(float),
        "age": rng.integers(18, 90, size=n).astype(float),
        "triage_vital_hr": rng.integers(50, 150, size=n).astype(float),
        "triage_vital_sbp": rng.integers(80, 180, size=n).astype(float),
        "triage_vital_dbp": rng.integers(40, 110, size=n).astype(float),
        "triage_vital_rr": rng.integers(10, 30, size=n).astype(float),
        "triage_vital_o2": rng.integers(85, 100, size=n).astype(float),
        "triage_vital_temp": rng.integers(96, 103, size=n).astype(float),
        "triage_glucose": rng.integers(70, 200, size=n).astype(float),
        "gender": rng.integers(0, 2, size=n),
        "cc_chestpain": rng.integers(0, 2, size=n),
        "cc_headache": rng.integers(0, 2, size=n),
    }
    return pd.DataFrame(data)


def test_clean_produces_valid_schema():
    """After cleaning, is the data the shape the model expects? Check the contract."""
    raw = _make_fake_raw(n=60)
    df = clean(raw)

    assert df[TARGET].isin([1, 2, 3, 4, 5]).all()          # only valid ESI labels
    for col in VITALS:
        assert df[col].isna().sum() == 0                    # no gaps after imputation
    assert len(df) > 0                                       # no empty frame


def test_smoke_train_predict():
    """Does the whole pipeline run on a tiny slice without crashing?"""
    raw = _make_fake_raw(n=60)
    df = clean(raw)

    feature_cols = VITALS + ["age"]
    X = df[feature_cols].fillna(0)
    y = df[TARGET]

    X_train, y_train = X.iloc[:45], y.iloc[:45]
    X_test, y_test = X.iloc[45:], y.iloc[45:]

    model = build_model("random_forest", {"n_estimators": 20}, seed=27)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    assert len(preds) == len(y_test)   # ran, right shape
