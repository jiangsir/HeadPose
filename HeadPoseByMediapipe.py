import cv2, time
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.mediapipe.python.solutions.face_mesh
mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing_utils = mp.solutions.mediapipe.python.solutions.drawing_utils
mp_drawing_utils.DrawingSpec(thickness=1, circle_radius=1)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cam.isOpened():
    success, img = cam.read()
    cv2.imshow('xxxx', img)
    if cv2.waitKey(5) & 0xFF == 27: # ESC
        break

cam.release()
