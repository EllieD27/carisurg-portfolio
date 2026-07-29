# Model-Selection Results Table

Audit trail for Martina Griffith (Clinical IT Lead) — every model trained across Weeks 6–7,
one row each, winner marked. Full reasoning: [`docs/week7-decision-journal.pdf`](week7-decision-journal.pdf).

Dataset: Yale EMMLC ED Triage Dataset (55,121 encounters) · Seed: 27 · Test set: 11,025 encounters
Primary metric ★: **ESI-1 Recall** — missing a critically ill patient is not recoverable; a false alarm is correctable.

| Model | Key hyperparameters | Accuracy | Macro Precision | Macro Recall | Macro F1 | ESI-1 Recall ★ | Train (s) | Infer (ms) | Interpretability |
|---|---|---|---|---|---|---|---|---|---|
| Dummy (stratified) | — | 0.372 | 0.200 | 0.200 | 0.200 | 0.000 | <0.1 | 0.0003 | N/A |
| Logistic Regression (Wk 6 baseline) | `max_iter=1000`, `class_weight=balanced` | 0.457 | 0.399 | 0.502 | 0.345 | 0.500 | 2.95 | 0.0006 | High |
| Decision Tree (Wk 6 baseline) | `max_depth=8`, `class_weight=balanced` | 0.375 | 0.336 | 0.320 | 0.261 | 0.125 | 0.27 | 0.0004 | High |
| **Random Forest + Threshold (Wk 7) ★ WINNER** | `n_estimators=300`, `class_weight=balanced`, `min_samples_leaf=2`, threshold=0.5×mean | **0.500** | 0.394 | 0.490 | 0.357 | **0.750** | 21.32 | 0.0571 | Medium |
| Gradient Boosting + Threshold (Wk 7, runner-up) | `n_estimators=300`, `learning_rate=0.1` | 0.627 | 0.466 | 0.380 | 0.366 | 0.188 | ~110.7 | 0.0185 | Low |
| MLP + Threshold (Wk 7) | `hidden_layer_sizes=(64,32)` | 0.444 | 0.412 | 0.351 | 0.311 | 0.500 | ~17.2 | 0.0025 | Low |

**Winning model: Random Forest + ESI-1 threshold tuning.** Raises ESI-1 Recall from 0.500
(Logistic Regression baseline) to 0.750 — correctly flagging 12 of 16 critically ill patients
in the held-out test set vs 8 of 16 — at Medium interpretability (feature importances, no SHAP
required) and a manageable one-off training cost of ~21–35s.

Threshold note: the ESI-1 decision threshold is derived from the **training** distribution only
(half the mean ESI-1 probability among true ESI-1 training patients) — no test data was used to
set it, preserving evaluation integrity.

Runner-up pinned for reference: Gradient Boosting has the highest raw accuracy (0.627) but the
worst ESI-1 Recall of the three complex models (0.188) and Low interpretability — rejected for
Phase 3 deployment on clinical-safety and governance grounds. Full trade-off discussion:
[`docs/week7_cost_benefit_memo.pdf`](week7_cost_benefit_memo.pdf).
