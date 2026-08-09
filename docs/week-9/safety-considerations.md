# Safety Considerations (One-Pager)

**Chosen implementation: Setting A — ED Triage Desk, HCI, portable/handheld tablet** (carried by the nurse, not desk-mounted).

---

### HCI (Setting A — chosen implementation)

**1. Alarm fatigue**
- Concern: excessive alerts cause nurses to start ignoring them.
- Context: nurses already manage monitor alerts, medication reminders, and call bells.
- Mitigation: alert only above a defined confidence threshold; distinguish high-confidence flags from low-confidence prompts.
- Residual risk: a threshold calibrated on a different population may be miscalibrated for Mercer's actual case mix.

**2. Display legibility under stress**
- Concern: an interface legible in calm conditions becomes illegible under clinical stress and variable lighting.
- Context: nurses read the screen while managing the patient in front of them — it must work at a glance.
- Mitigation: 16pt minimum font, WCAG AA contrast, critical info top-left.
- Residual risk: individual variation in visual acuity/stress response — no single design works for everyone.

**3. Device loss or damage mid-shift** 
- Concern: a dropped or misplaced device removes the tool from use exactly when it's needed, and risks a data exposure if lost.
- Context: constant movement between desk, queue, and bedside increases handling and drop opportunities compared to a fixed terminal.
- Mitigation: drop-rated case, secure strap, auto-lock/encryption, remote wipe on reported loss, and a manual-process fallback that doesn't depend on the device at all.
- Residual risk: a fallback to fully manual triage removes the tool's benefit entirely for that assessment — an acceptable but real degradation.

### HRI (Setting B — comparison, not implemented)

**1. Voice input failure in noisy conditions**
- Concern: ED ambient noise causes high error rates in voice recognition.
- Context: generator noise, HVAC, and patient volume exceed standard voice-recognition thresholds.
- Mitigation: voice supplementary only; touch/button alternative for all critical interactions; confirmation required before execution.
- Residual risk: confirmation steps add time, which may reduce willingness to use voice input at all.

**2. Graceful degradation when sensors fail**
- Concern: sensor failure could produce an incorrect classification or halt the assessment mid-patient.
- Context: power fluctuation and humidity-related equipment failure are foreseeable in Caribbean clinical infrastructure.
- Mitigation: switch to manual entry fallback; alert the nurse; log the failure; never classify on partial data without flagging the gap.
- Residual risk: a nurse mid-shift may not have time to respond to a manual fallback request, resulting in no classification.

**3. Physical proximity and trust**
- Concern: a robot operating close to a patient who may not be able to move away raises both safety and trust concerns not present with a screen.
- Context: patients may not expect or understand why a robotic system is involved in their care.
- Mitigation: defined minimum safe distance, visible/audible presence indicators, and a clear informed-consent step distinct from the HCI setting's lighter consent requirement.
- Residual risk: even with consent given, physical unease may not be fully mitigated — this is a structurally higher-trust-burden setting, which is part of why Setting A was chosen for this pilot.
