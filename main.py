import cv2

cap = cv2.VideoCapture('videos/cars.mp4')

while True:
    frames_left, frame = cap.read()

    if not frames_left:
        break

    cv2.imshow('This is the title of the frame', frame)

    key = cv2.waitKey(10)

    ESC = 27
    if key == ESC:
        break