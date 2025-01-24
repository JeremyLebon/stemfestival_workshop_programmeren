import cv2
import numpy as np
import time

def main():
# Open the first available camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Error: Could not open camera.')
        return

    ret, frame = cap.read()
  
    cv2.imshow('Original', frame)
  
    time.sleep(5)
  
    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
