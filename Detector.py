import cv2 as cv
import mediapipe as mp


class FaceDetector():

	def __init__(self, minDetectionCon = 0.5):
		self.minDetectionCon = minDetectionCon

		self.fd = mp.solutions.face_detection.FaceDetection(self.minDetectionCon) 
		self.draw = mp.solutions.drawing_utils # used for drawing on the image (easy way)

	def findFaces(self, image, draw=True):
		img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		ih, iw, ic = img.shape
		self.results = self.fd.process(img)

		bboxs = [] # return a list of bounding boxes
		if self.results.detections:
			for id, detection in enumerate(self.results.detections):
				bboxN = detection.location_data.relative_bounding_box
				bbox = int(bboxN.xmin * iw), int(bboxN.ymin * ih), int(bboxN.width * iw), int(bboxN.height * ih) # normalized --> pixel value

				bboxs.append([id, bbox, detection.score])
				
				if draw:
					image = self.niceDraw(image, bbox)

					# cv.putText(image, f'{int(detection.score[0] * 100)}%', 
					# 		  	(bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN,
					# 	  		 2, (255, 0, 255), 2 )
		return image, bboxs # return the bounding boxes && image that has those detections on it 


	def niceDraw(self, img, bbox, l=30, t=5, rt=1): # take a bbox at each time (don't pass it a list of bbox).
		x, y, w, h = bbox
		x1, y1 = x+w, y+h # bottom points
		
		# l --> length of the line, t --> thickness, rt --> rectangle thickness
		cv.rectangle(img, bbox, (255, 0, 255), rt)

		# top left x,y
		cv.line(img, (x,y), (x+l, y), (255, 0, 255), t)
		cv.line(img, (x,y), (x, y+l), (255, 0, 255), t)

		# top right x1,y
		cv.line(img, (x1,y), (x1-l, y), (255, 0, 255), t)
		cv.line(img, (x1,y), (x1, y+l), (255, 0, 255), t)

		# bottom left x,y1
		cv.line(img, (x,y1), (x+l, y1), (255, 0, 255), t)
		cv.line(img, (x,y1), (x, y1-l), (255, 0, 255), t)

		# bottom right x1,y1
		cv.line(img, (x1,y1), (x1-l, y1), (255, 0, 255), t)
		cv.line(img, (x1,y1), (x1, y1-l), (255, 0, 255), t)



		return img


if __name__ == "__main__":
	main()