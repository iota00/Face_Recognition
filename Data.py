import pickle as pk
import os
import face_recognition as fr



def save_data(labels, faces):
	pk_labels = open('labels.pickle', 'wb')
	pk_faces = open('faces.pickle', 'wb')
	pk.dump(labels,pk_labels)
	pk.dump(faces,pk_faces)
	pk_labels.close()
	pk_faces.close()

def append_data(labels, faces):
	pk_labels = open('labels.pickle', 'ab')
	pk_faces = open('faces.pickle', 'ab')
	pk.dump(labels,pk_labels)
	pk.dump(faces,pk_faces)
	pk_labels.close()
	pk_faces.close()
	

def load_data():
	pk_labels = open('labels.pickle', 'rb')
	pk_faces = open('faces.pickle', 'rb')
	labels = pk.load(pk_labels)
	faces = pk.load(pk_faces)
	pk_labels.close()
	pk_faces.close()

	return labels, faces
	
def encode_faces(labels):
	names = []
	encodings = []
	for label in labels :
		for image in os.listdir(label):
			
			try:
				image_path = os.path.join(label, image)
				person_img = fr.load_image_file(image_path)
				person_img_encoding = fr.face_encodings(person_img)[0]

				print(f'[+] {label} Added')
				# print()
				encodings.append(person_img_encoding)
				names.append(label)

			except:
				print(f'[-] Oops! something went wrong with {image_path} file!!')
		

	return names, encodings
