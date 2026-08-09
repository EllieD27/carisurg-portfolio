# System Requirements

### Inputs
- Primary: EHR pull (age, presenting complaint, recent vitals) via Mercer's EHR API.
- Fallback: manual entry, reachable within 2 user actions if EHR pull fails or Wi-Fi drops.
- No device/sensor stream in this implementation.

### Outputs
- Colour-coded alert (red/amber/green) + numeric score (1–5) + icon/shape differentiator (never colour alone).
- Top 2–3 contributing features in plain language.
- Low-confidence flag when applicable, prompting manual review rather than false certainty.

### Human Action Required
- Nurse reviews and confirms or overrides within the triage window; every override logged with a reason, timestamp, and reversible record.

### Functional Requirements
1. The interface must display the triage classification within 1.5 seconds of input submission.
2. The system must provide a nurse override mechanism that logs the reason for the override.
3. The device must auto-lock on inactivity or when set down, requiring re-authentication to resume.

### Non-Functional Requirements
1. The interface must remain legible under fluorescent clinical lighting at up to 1 metre.
2. The system must degrade gracefully to manual entry fallback within 5 seconds of an EHR/Wi-Fi connectivity failure.
3. The device must withstand a standard waist-height drop without loss of function (or fail cleanly into the manual fallback path).

### Integration Requirements
1. The system must pull from the Mercer EHR API where available; in its absence, manual entry must be reachable within 2 user actions.
2. The device must connect only to Mercer's internal Wi-Fi network, with encrypted data in transit and device-level (not shared-login) authentication.
3. Remote lock/wipe capability must be available and triggerable only on an explicit lost/stolen report — not on routine connectivity loss, to avoid conflicting with the offline-fallback requirement.