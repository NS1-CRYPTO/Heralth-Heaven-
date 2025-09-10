# Video Storyboard & Recording Instructions

Recording tips:
- Use OBS Studio to capture screen and webcam.
- Record each scene separately (web UI, terminal, Pi camera) and edit together.
- Add subtitles for accessibility.

OBS simple recording commands (example):
- Start OBS, set 'Display Capture' and 'Video Capture Device'.
- Use a 16:9 canvas, 1920x1080, 30fps.
- Record each clip, then use simple editor (Shotcut / OpenShot).

Command-line demo steps to capture in the video:
1. Start server: `./run_demo.sh`
2. Use curl to call API (for terminal view):
   ```
   curl -X POST "http://localhost:8000/triage/text" -H "Content-Type: application/json" -d '{"patient_age":30,"patient_sex":"F","presenting_complaint":"red painful leg","vitals": {"temp":38.7}}'
   ```
3. Show response JSON and highlight urgency + recommendations.
