import cv2
import numpy

# Setting up the Face and Smile Detector

## load some pre trained data on face data from https://github.com/opencv/opencv/tree/4.x/data/haarcascades
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
## load some pre trained data on face data from https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_smile.xml
smile = cv2.CascadeClassifier('haarcascade_smile.xml')


### This is Static Picture Code

'''
# image to detect faces in
img = cv2.imread('download.jpeg')

# convert to greyscale
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = face.detectMultiScale(grayscaled_img)

# draw green rectangle around face hard coded
cv2.rectangle(img, (86, 21), (86+96, 21+96), (0,255,0), 2 )

# draw a green rectangle around face dynamically
(x, y, w, h) = face_coordinates[0]
cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2 )

# show the location of face in image
# print(face_coordinates)

# this will show the image
cv2.imshow('Clever Programmer Face Detector', img)

# this will keep the image open till a key is pressed
cv2.waitKey()
'''

### This is Webcam code

# To capture video from webcam
webcam = cv2.VideoCapture(1) # one face defaulted to webcam. Add a video path instead.

# Iterate forever over frames
while True:
    # read the current frame from the webcam video stream
    successful_frame_read, frame = webcam.read()
    
    # if theres and error, abort
    if not successful_frame_read:
        break
    
    # convert to image to greyscale as this is easier to calculate, therefore less processing.
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # detect faces
    faces = face.detectMultiScale(grayscaled_img,1.3,5)
    
    # run face detection within each of the faces
    for (x, y, w, h) in faces:
        
        # draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100,200,50), 4 )
        
        # get the sub frame (using numpy N-dimensional array slicing)
        the_face = frame[y:y+h, x:x+w]
        
        # change to greyscale
        face_grayscale = cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
        
        smiles = smile.detectMultiScale(face_grayscale,scaleFactor=1.7, minNeighbors=20)
        
        # find all smiles in the face
        for (x_, y_, w_, h_) in smiles:
            
            # draw rectangles around the smile
            cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (0,255,0), 2)
            
        # label this face as smiling
            if len(smiles) > 0:
                cv2.putText(frame, 'Smiling', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))
        
    # this will show the image
    cv2.imshow('bobdatcod.e Face Booth', frame)
    
    # Display
    key = cv2.waitKey(1)
    
    # Stop if Q key is pressed
    ''' 81 is the ascii code for q'''
    if key == 81  or key == 113:
        break

# Release the VideoCapture object
webcam.release()
cv2.destroyAllWindows()

print('Code Completed')