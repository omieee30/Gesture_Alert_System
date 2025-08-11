import os

# Project structure
project_name = "gesture_alert_system"
folders = [os.path.join(project_name, "venv")]
files = {
    os.path.join(project_name, "main.py"): """import cv2
import mediapipe as mp
import playsound

def detect_gesture(frame):
    # TODO: Add gesture detection logic
    return False

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if detect_gesture(frame):
            playsound.playsound('alarm.wav')

        cv2.imshow("Gesture Alert System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
""",
    os.path.join(project_name, "requirements.txt"): "opencv-python\nmediapipe\nplaysound\nnumpy\n",
    os.path.join(project_name, "alarm.wav"): "",  # Placeholder
    os.path.join(project_name, "setup.bat"): f"""@echo off
python -m venv venv
call venv\\Scripts\\activate
pip install -r requirements.txt
echo Setup complete!
pause
""",
    os.path.join(project_name, "run.bat"): f"""@echo off
call venv\\Scripts\\activate
python main.py
pause
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Project '{project_name}' created successfully with setup.bat and run.bat!")
