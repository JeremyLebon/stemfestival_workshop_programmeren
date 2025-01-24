import cv2
import numpy as np

def main():
    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    while True:
        # Capture frame from the camera
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        frame_lines = frame.copy()

        # Apply GaussianBlur to reduce noise and improve edge detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges using Canny edge detector
        edges = cv2.Canny(blurred, 50, 150)

        # Display the frame with detected triangles
        cv2.imshow("Standard frame", frame)

        cv2.imshow("Lines", edges)
        

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
