"""
src/features.py — engineer & encode

Turns the cleaned DataFrame into the (X, y) feature matrix used for
training. Extracted from the notebook's feature-selection cell — 7 vitals
+ age + chief-complaint flags with prevalence >= 0.5%.
"""

import pandas as pd
from .data import VITALS, TARGET


def select_features(df: pd.DataFrame, min_cc_prevalence: float = 0.005) -> list:
    """
    Return the feature column list: 7 vitals + age + every cc_* (chief
    complaint) binary flag with prevalence >= min_cc_prevalence.

    Demographic columns (gender, ethnicity, race, etc.) are excluded by
    default — see docs/model-selection.md and the Week 5 fairness memo for
    why demographic encoding is off unless explicitly re-enabled.
    """
    cc_cols = [c for c in df.columns if c.startswith("cc_")]
    usable_cc = [c for c in cc_cols if df[c].mean() >= min_cc_prevalence]
    return VITALS + ["age"] + usable_cc


def build_xy(df: pd.DataFrame, features: list = None):
    """Build the (X, y) matrix. Missing feature values are filled with 0."""
    if features is None:
        features = select_features(df)
    X = df[features].fillna(0)
    y = df[TARGET]
    return X, y


def encode_demographics(X: pd.DataFrame, df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    """
    Optional one-hot encoding of demographic columns. OFF by default —
    only call this explicitly if a fairness-audited use case requires it.
    """
    if columns is None:
        columns = []
    if not columns:
        return X
    demo = pd.get_dummies(df[columns], prefix=columns)
    return pd.concat([X.reset_index(drop=True), demo.reset_index(drop=True)], axis=1)
