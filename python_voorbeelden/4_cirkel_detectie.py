import cv2
import numpy as np

def main():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise and improve circle detection
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)

        # Use the Hough Circle Transform to detect circles
        circles = cv2.HoughCircles(
            blurred,                       # Input image (grayscale)
            cv2.HOUGH_GRADIENT,            # Detection method
            dp=1.2,                        # Inverse ratio of accumulator resolution to image resolution
            minDist=50,                    # Minimum distance between detected circles
            param1=50,                     # Higher threshold for Canny edge detection
            param2=30,                     # Threshold for center detection (lower is more sensitive)
            minRadius=5,                  # Minimum circle radius
            maxRadius=30                  # Maximum circle radius
        )

        # If circles are detected, draw them
        if circles is not None:
            circles = np.uint16(np.around(circles))  # Convert circle parameters to integers
            for circle in circles[0, :]:
                x, y, r = circle  # x, y (center) and r (radius)
                # Draw the circle
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)  # Green circle outline
                # Draw the center
                cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)  # Red dot at the center

        # Display the output
        cv2.imshow("Circle Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
