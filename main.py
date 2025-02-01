import cv2
import ctypes

WINDOW_NAME = 'Cars tracking'
cap = cv2.VideoCapture('videos/cars.mp4')


def get_monitor_proportions() -> tuple[int, int]:
    user32 = ctypes.windll.user32

    window_x = user32.GetSystemMetrics(0)
    window_y = user32.GetSystemMetrics(1)

    return (window_x, window_y)


while True:
    frames_left, frame = cap.read()

    if not frames_left:
        break

    window_x, window_y = get_monitor_proportions()
    resized_frame      = cv2.resize(frame, (window_x, window_y))

    cv2.imshow(WINDOW_NAME, resized_frame)
    cv2.moveWindow(WINDOW_NAME, 0, 0)

    key = cv2.waitKey(10)

    ESC = 27
    if key == ESC:
        break