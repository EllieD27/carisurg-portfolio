# Seven-Axis Benchmark Table — Week 7

| Model | Accuracy | Macro F1 | ESI-1 Recall ★ | Train (s) | Infer (ms) | Interpretability |
|---|---|---|---|---|---|---|
| Dummy (stratified) | 0.372 | 0.200 | 0.000 | 0.01 | 0.0003 | N/A |
| Logistic Regression (baseline) | 0.457 | 0.345 | 0.500 | 7.67 | 0.0011 | High |
| Decision Tree (baseline) | 0.375 | 0.261 | 0.125 | 0.34 | 0.0005 | High |
| Random Forest (Week 7) | 0.610 | 0.393 | 0.000 | 35.79 | 0.0747 | Medium |
| Random Forest + Threshold (Week 7) | 0.500 | 0.357 | 0.750 | 35.79 | 0.0747 | Medium |

★ **Primary metric: ESI-1 Recall.**
Missing a critically ill patient is not recoverable; a false alarm is.

*Saved to `../docs/week7_benchmark_table.csv`*
