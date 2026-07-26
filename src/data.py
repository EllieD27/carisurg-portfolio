"""
src/data.py — load & clean

Everything that turns the raw CSV into a modelling table.
Extracted from week7_complete_models_eval.ipynb, section 1
("Data preparation — identical pipeline to Week 6"). Logic unchanged —
only restructured into named, importable, testable functions.
"""

import pandas as pd
import numpy as np

TARGET = "esi"

VITALS = [
    "triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp",
    "triage_vital_rr", "triage_vital_o2", "triage_vital_temp", "triage_glucose",
]

# Plausible physiological ranges — values outside these are treated as
# data-entry errors and set to NaN before imputation.
PLAUSIBLE = {
    "age": (0, 120), "esi": (1, 5),
    "triage_vital_hr": (20, 250), "triage_vital_sbp": (50, 300),
    "triage_vital_dbp": (20, 200), "triage_vital_rr": (4, 60),
    "triage_vital_o2": (50, 100), "triage_vital_temp": (86, 110),
    "triage_glucose": (20, 800),
}

# Columns known only AFTER triage — excluded as leakage risks.
LEAKAGE_COLS = ["disposition", "previousdispo"]


def load_raw(path: str) -> pd.DataFrame:
    """Read the raw CSV into a DataFrame."""
    df = pd.read_csv(path, index_col=0, on_bad_lines="skip")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Coerce vitals to numeric, null out implausible values, drop rows with
    no ESI label, impute vitals with the median, and round/cast ESI to int.

    Mirrors the Week 6/7 notebook cleaning cell exactly — only the target
    column is required to be present in `df`.
    """
    df_clean = df[df[TARGET].notna()].copy()

    for col in VITALS + ["age"]:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

    for col, (lo, hi) in PLAUSIBLE.items():
        if col in df_clean.columns:
            mask = (df_clean[col] < lo) | (df_clean[col] > hi)
            df_clean.loc[mask, col] = np.nan

    for col in VITALS:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    df_clean[TARGET] = df_clean[TARGET].round().astype(int)

    return df_clean
