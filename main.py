from fr_video_module import face_video_recog as FVR
from fr_image_module import face
from os import system
from cv2 import destroyAllWindows, waitKey

ensa = r'''
     ______     ___      ____   ________    ____
    /  ___/    /   \    /   /  /  _____/   /    \
   /  /___    /     \  /   /  /  /____    /  /\  \
  /  ____/   /   /\  \/   /  /____   /   /  /__\  \
 /  /___    /   /  \     /   ____/  /   /    __    \
/______/   /___/    \___/   /______/   /____/  \____\

'''

menu = r'''
[*]	Welcome to the face recognition program:
	
	1. Faces on an image
	2. Faces on a video
	3. Exit
'''

print(ensa)
print(menu)

while True:
	system('clear')
	print(ensa)
	print(menu)

	c = input('Your choice: ')

	while not len(c) or int(c) not in [1,2,3]:
		print('\n[!] You choose a wrong choise, try again')
		c = input('Your choice: ')

	if int(c) == 1:
		path = input('[*] Path to the image: ')
		face(path)
	elif int(c) == 2:
		path = input('[*] Path to the video file (0 or empty to use the webcam):')
		FVR(path)
	else:
		from time import sleep as s
		print('[*] Thank for using the program, ...')
		s(1)
		break	

quit()










