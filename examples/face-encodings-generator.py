# load necessary libraries
import face_recognition, glob
import csv

# loading image folders
folders = glob.glob('../data/train/*')
columns = ["fe"+str(i+1) for i in range(128)]
case = 0

# creating csv file
with open('../data/train-face-encodings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Case#', 'name', *columns])
    #looping through folder
    for i, folder in enumerate(folders):
        #storing files in a variable
        files = glob.glob(folder + '/*')
        #looping through files
        for file in files:
            #storing file in image
            image = face_recognition.load_image_file(file)
            # determining face location
            face_location = face_recognition.face_locations(image, number_of_times_to_upsample=2)
            # determing face encodings
            known_face_encoding = face_recognition.face_encodings(image, known_face_locations=face_location)[0]
            case += 1
            # writes to the csv file
            writer.writerow([case, folder.split('\\')[-1], *known_face_encoding])
