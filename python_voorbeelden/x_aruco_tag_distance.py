import cv2
import numpy as np

def main():
    # Load the predefined dictionary of ArUco markers
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    camera_matrix = np.array([[1000,    0, 960],  # fx, 0, cx
                          [   0, 1000, 540],  # 0, fy, cy
                          [   0,    0,   1]], dtype=np.float64)  # 0, 0, 1
    dist_coeffs = np.array([-0.1, 0.1, 0, 0, 0], dtype=np.float64)  # Example distortion coefficients

    # Create a detector parameters object
    parameters = cv2.aruco.DetectorParameters()

    # Initialize the camera
    cap = cv2.VideoCapture(1)  # Use your camera (index 0 for the first camera)

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
            marker_length = 0.05  # in meters

            # Estimate pose
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)

            
            for i in range(len(ids)):
                # Get the translation vector (tvec) for each marker
                rvec = rvecs[i]
                tvec = tvecs[i]

               # Draw axis for visualization
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)
                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.1)

                # Calculate distance (Euclidean norm of tvec)
                distance = np.linalg.norm(tvec)

                # Display the distance on the marker
                text = f"ID: {ids[i][0]} Distance: {distance:.2f} m"
                cv2.putText(frame, text, (int(corners[i][0][0][0]), int(corners[i][0][0][1] - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            

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


        