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

        # Use the cvtColor() function to grayscale the image
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the original frame and the edge-detected frame
        cv2.imshow('Original', frame)
        cv2.imshow('Grayscale', gray_image)
      
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()