# VIVES Stem festival: workshop programmeren

[OpenCV on web](https://opencv.onweb.dev/)


## Inlezen van de camera

````python
import cv2
import numpy as np

def main():
# Open the first available camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Error: Could not open camera.')
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print('Error: Could not read frame.')
            break

        # Display the original frame and the edge-detected frame
        cv2.imshow('Original', frame)
      
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


````



import cv2
import numpy as np

def main():
    # Open the first available camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Error: Could not open camera.')
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print('Error: Could not read frame.')
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Perform edge detection using Canny
        edges = cv2.Canny(blurred, 50, 150)

        # Display the original frame and the edge-detected frame
        cv2.imshow('Original', frame)
        cv2.imshow('Edges', edges)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
