Sign Language Recognition App

Overview

This is an OpenCV-based application that uses MediaPipe to detect and recognize American Sign Language (ASL) letters. Users can hold up a hand sign in front of their camera, and the app will identify the corresponding letter in real time. The application tracks the right hand, detecting finger joints and landmarks to interpret the sign based on their relative positioning.

Features

Real-Time Hand Tracking: Uses MediaPipe to create hand landmarks and track finger joints.

Sign Language Recognition: Identifies ASL letters based on hand gestures.

Interactive Camera Feed: Displays a live camera feed with overlaid hand landmarks and the detected letter.

How It Works

The app captures video from the user's webcam using OpenCV.

MediaPipe processes the video frames to detect hand landmarks.

Based on the position of the finger joints and landmarks, the app determines which ASL letter is being shown.

The detected letter is displayed on the video feed.

Requirements

Python 3.6+

OpenCV

MediaPipe

Installation

To install the required packages, run the following command:

pip install opencv-python mediapipe

Usage

Clone or download the project to your local machine.

Save the provided code as sign_language_recognizer.py.

Run the script using the following command:

python sign_language_recognizer.py

The app will open a live video feed from your webcam.

Hold up an ASL sign with your right hand while facing the camera.

The detected letter will be displayed on the video feed.

Press 'q' to quit the application.

Supported Letters

The app recognizes the following ASL letters based on hand gestures:

A

B

C

D

E

F

G

H

I

J

K

L

M

N

O

P

Q

R

S

T

U

V

W

X

Y

Important Notes

Use Your Right Hand: The app is designed to recognize signs made with the right hand.

Face the Camera: Ensure that your hand is fully visible to the camera for accurate detection.

Lighting Conditions: For best results, use the app in a well-lit environment.

Troubleshooting

If the app cannot detect your hand, check your webcam connection and ensure that you are using the correct camera index (cap = cv2.VideoCapture(0) for default camera).

If the recognition is inaccurate, try adjusting the lighting and ensuring that your hand is clearly visible to the camera.

Future Improvements

Adding support for more ASL signs and gestures.

Improving accuracy for left-hand recognition.

Adding a graphical user interface (GUI).

License

This project is open-source and available for use and modification.
