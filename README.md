# Stay-Awake-App

## Mission
Stay Awake App is a proactive computer vision application designed to detect when a student has fallen asleep at their laptop and emit a sound to awaken them. This project is born out of the common student experience of burning the midnight oil, only to unintentionally drift off while studying or working on an assignment. 

## How it Works
Using advanced computer vision techniques, the Stay Awake App monitors your eyes through the webcam. If it detects that your eyes have been closed for a certain threshold of time, it concludes that you might have dozed off and plays a sound to wake you up.

## Features
- Real-time eye tracking to detect when the user is likely asleep.
- Audio alert to wake the user from their unintended nap.

## Getting Started
### Prerequisites
- A webcam
- Python 3.6+
- OpenCV, MediaPipe, and Pygame

### Installation & Usage
1. Clone the repository:
   ```shell
   git clone https://github.com/Abdessamadae/stay-awake-app.git
2. Run:
   ```bash
   pip install opencv-python mediapipe pygame
4. Run:
    ```bash
    python wakeup_alert.py

### Customization
You can customize the following parameters within the script:

1. Sound File: Change the sound file to any .wav file of your choice.
2. Sensitivity: Adjust the time threshold to avoid false positives from normal blinking.
   
