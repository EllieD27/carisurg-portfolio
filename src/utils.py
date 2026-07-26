"""
src/utils.py — shared helpers
"""

import yaml


def load_config(path: str) -> dict:
    """Load config.yaml into a plain dict."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def format_benchmark_row(name: str, metrics: dict, train_s: float, infer_ms: float, interpretability: str) -> dict:
    """Format one model's metrics into a row matching docs/model-selection.md."""
    return {
        "Model": name,
        "Accuracy": f"{metrics['accuracy']:.3f}",
        "Macro Precision": f"{metrics['macro_precision']:.3f}",
        "Macro Recall": f"{metrics['macro_recall']:.3f}",
        "Macro F1": f"{metrics['macro_f1']:.3f}",
        "ESI-1 Recall": f"{metrics['esi1_recall']:.3f}",
        "Train (s)": f"{train_s:.2f}",
        "Infer (ms)": f"{infer_ms:.4f}",
        "Interpretability": interpretability,
    }
