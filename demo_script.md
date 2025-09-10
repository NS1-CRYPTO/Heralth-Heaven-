# 3-minute Demonstration Video Script — ClinicAssist

Total length: 3:00

0:00-0:08 — Title card (5s)
  - "ClinicAssist — Offline gpt-oss Triage Agent"
  - Overlay: Hackathon category: Best Local Agent

0:08-0:25 — One-line problem statement (17s)
  - Narrator: "In low-resource clinics, clinicians need offline decision support for triage and referrals."
  - Show: clinic setting photo, Raspberry Pi + USB camera.

0:25-0:45 — Quick architecture (20s)
  - Show animated diagram: Camera → Local Server (gpt-oss) → GUI / SMS / Printout.
  - Narrator: "Runs fully locally, supports speech->text, images, and provides structured JSON outputs."

0:45-2:20 — Live demo (95s)
  - Scene A (30s): Enter case in web UI (age, sex, complaint). Send.
  - Scene B (30s): Upload wound photo. Server processes and returns triage JSON.
  - Scene C (35s): Show generated referral letter and suggested meds. Show local log saving.

2:20-2:50 — Robustness & safety (30s)
  - Narrator: "Safety layers: structured JSON, red-flag detection, local logging, human-in-the-loop."
  - Show pros/cons and fail-safes.

2:50-3:00 — Closing (10s)
  - Call-to-action: "Code + instructions in repository. Thank you!"
