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
    success, frame = cap.read()

    if not success:
        break

    proportions: tuple = get_monitor_proportions()
    frame = cv2.resize(frame, proportions)

    cv2.imshow(WINDOW_NAME, frame)
    cv2.moveWindow(WINDOW_NAME, 0, 0)

    key = cv2.waitKey(10)

    ESC = 27
    if key == ESC:
        break


cap.release()
cv2.destroyAllWindows()