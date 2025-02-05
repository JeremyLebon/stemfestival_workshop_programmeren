import cv2
import numpy as np

def main():
    # Start video capture from the webcam
    cap = cv2.VideoCapture(1)
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

        # Apply GaussianBlur to reduce noise and improve edge detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges using Canny edge detector
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Approximate the contour to a polygon
            epsilon = 0.02 * cv2.arcLength(contour, True)  # Accuracy for approximation
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Check if the polygon has 4 sides
            if len(approx) == 4:
                # Draw the detected square or rectangle on the frame
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

        # Display the frame with detected squares
        cv2.imshow("Detected Squares", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
