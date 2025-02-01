import cv2
import ctypes

user32 = ctypes.windll.user32

window_x = user32.GetSystemMetrics(0)
window_y = user32.GetSystemMetrics(1)

print(f'MONITOR WIDTH:  {window_x}')
print(f'MONITOR HEIGHT: {window_y}')

window_center_x = int(window_x / 2)
window_center_y = int(window_y / 2)

print(f'MONITOR CENTER WIDTH:  {window_center_x}')
print(f'MONITOR CENTER HEIGHT: {window_center_y}')

cap = cv2.VideoCapture('videos/cars.mp4')

# while True:
#     frames_left, frame = cap.read()

#     if not frames_left:
#         break

#     cv2.imshow('This is the title of the frame', frame)

#     key = cv2.waitKey(10)

#     ESC = 27
#     if key == ESC:
#         break