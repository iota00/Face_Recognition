# [*] import required libs

import face_recognition as fr
import cv2 as cv
from Detector import FaceDetector as fd
from numpy import argmin
from Data import load_data

'''
[*] face_image_recog --> take as argument :
    - the unknown image that we wanna process

'''

def face_image_recog(image): # --> get the image from the detector 
    try:
        # Encode the image
        image_encode = fr.face_encodings(image)[0]

        # Load the data
        labels, faces = load_data()

        
        # matches = fr.compare_faces(faces, unknown_img_enc)
        
        # A simple way of finding the correct match is to take the min of the distances calculed, we can aslo use the .compare_faces() function
        dist = fr.face_distance(faces, image_encode)
        
        # Find the index of the lowest distance value within the distances array
        index = argmin(dist)

        # Get the label (name) that belongs to that index
        label = labels[index]

        # Return the label and the image
        return label.upper() ,image

    except:
        # In case of any error* the function will return the word 'Unknown' as label
        return 'Unknown', image

# (*): there is a lot of error types that can be occoured, but most of the time we get error we trying to encode the image 

'''
[*] the face() function takes 2 arguments:
    - the path to the image (prints an error message in case the path isn't specified)
    - the draw variable to determine id we want to draw the square around the face(s) in the image

'''

def face(path, draw=True):
    # Check if a path is specified or not
    if not len(str(path)):
        print('Error: please specify a correct path')

        return

    try:
        # Read the image with OpenCV
        image = cv.imread(path)

        # create the an instance of the detector
        detector = fd()

        # Find face and their location in the image frame (returns the image, and bounding boxes) + it draws the square around the faces it found
        image, bboxs = detector.findFaces(image, draw)

        # Print the file name
        print(f"Faces in : {path.split('/')[-1]}")

        # Loop throght the bboxs and get each bbox
        for box in bboxs:
            
            # Extract infomation from each box --> the id of the face, the bbox contains the face location, the score or prediction value
            id, bbox, score = box

            # Extract the face location information
            x,y,w,h = bbox

            # A margin used to help when trying to extract the face from the image
            l = 20

            # Extract the face from the image
            img = image[y - l:y + h + l, x - l:x + w + l]

            # Pass the face extracted to face_image_recog() function to process it and compare it with faces in the DB
            label, img = face_image_recog(img)

            # Write the label on the image
            cv.putText(image, label, (x,y - l), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2 )
            
            # Just a nice way of printing things on the console
            if label == 'unknown':
                print(f'[-]  {label}')
            else:
                print(f'[+]  {label}')

            # Show the image
        cv.imshow("image", image)
        cv.waitKey(0)

    except:
        print('[-] Error: Something went wrong')
        print('[...] Maybe you misstyped the path!')
        print('[...] Maybe the given image is corrupted!')
        



# face('test/jb1.jpg')
# face('test/jb2.jpg')
# import os

# for image in os.listdir('test'):
#   path = os.path.join('test', image)
#   face(path)