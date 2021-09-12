'''
[*] import required libs
'''

import cv2 as cv # --> OpenCV
from Detector import FaceDetector as fd
from fr_image_module import face_image_recog 

'''
[*] face_video_recog --> take as argument :
	- the path to the video file (if no path specified, it'll use the webcam by default)
	- the draw variable is used to tell the program to draw the box around the face or not

'''
def face_video_recog(path=0, draw=True):
	# if no path specified, the program will use the webcam by default
	if not len(str(path)) or path == '0':
		path = 0
	print("[!] press 'q' to quit")
	try:
		capture = cv.VideoCapture(path)
		# create the an instance of the detector
		detector = fd()

		while True:
			# Read data from the video
			success, frame = capture.read() 

			# Find face and their location in the image frame (returns the image, and bounding boxes) + it draws the square around the faces it found
			frame, bboxs = detector.findFaces(frame, draw)
			

			# Loop throght the bboxs and get each bbox
			for box in bboxs:
				id, bbox, score = box
				x,y,w,h = bbox
				# print(bbox)
				l = 30
				# Extract the face image from the frame 
				img = frame[y - l:y + h + l, x - l:x + w + l]

				# Pass the face extracted to face_image_recog() function to process it and compare it with faces in the DB
				label, image = face_image_recog(img)

				# Write the label on the image
				cv.putText(frame, label, (x,y - l//2), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2 )
				
				# Show the frame
				cv.imshow("Video", frame)

			# Stop and break out of the loop
			if cv.waitKey(1) & 0xFF == ord('q'):
				cv.destroyAllWindows()
				break
	except:
	        print('[-] Error: Something went wrong')
	        print('[...] Maybe you misstyped the path!')
	        print('[...] Maybe the given video is corrupted!')

# face_video_recog('video/mz1.mp4')