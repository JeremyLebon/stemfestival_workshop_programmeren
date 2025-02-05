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

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range for red color in HSV
        lower_red_1 = np.array([0, 70, 50])     # Lower red hue
        upper_red_1 = np.array([10, 255, 255])  # Upper red hue
      
        # Create masks for both ranges of red
        mask_red_1 = cv2.inRange(hsv_frame, lower_red_1, upper_red_1)
     
        # Apply the mask to the original frame
        red_only = cv2.bitwise_and(frame, frame, mask=mask_red_1)

        # Display the original frame and the red-filtered frame
        cv2.imshow('Original', frame)
        cv2.imshow('Red Filtered', red_only)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
