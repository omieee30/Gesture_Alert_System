# Gesture Alert System

_A real-time gesture-controlled emergency alert system built over a weekend._

**What it does:**
- Detects a “cross” hand gesture using MediaPipe + OpenCV
- Sends an SMS and an automated call via Twilio
- Displays a blurred video feed with hand landmarks — privacy-friendly display

**Tech Stack:**
- Python 3.x
- OpenCV
- MediaPipe
- Twilio REST API

**How to run:**
1. Install dependencies: `pip install -r requirements.txt`
2. Replace Twilio credentials in the script (`ACCOUNT_SID`, `AUTH_TOKEN`, etc.)
3. Run: `python gesture_alert.py`

**Potential Use Cases:**
- Silent emergency alerts
- Elderly/patient assistance
- Hands-free alert systems in industrial environments

**License:**
MIT License

---

