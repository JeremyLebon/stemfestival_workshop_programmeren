import cv2
import numpy as np

def main():
    # Load the predefined dictionary of ArUco markers
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    # Create a detector parameters object
    parameters = cv2.aruco.DetectorParameters()

    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Use your camera (index 0 for the first camera)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture a frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to grayscale (ArUco detection works better in grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect ArUco markers in the grayscale frame
        corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        # Draw detected markers on the original frame
        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            print(f"Detected IDs: {ids.ravel()}")  # Print the IDs of detected markers

        # Display the output
        cv2.imshow('ArUco Marker Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
