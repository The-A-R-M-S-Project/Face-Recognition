# load necessary libraries
import face_recognition, glob
import csv

folders = glob.glob('../data/test/*')
columns = ["fe"+str(i+1) for i in range(128)]
case = 0

with open('../data/test-face-encodings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Case#', 'name', *columns])
    for i, folder in enumerate(folders):
        files = glob.glob(folder + '/*')
        for file in files:
            image = face_recognition.load_image_file(file)
            face_location = face_recognition.face_locations(image, number_of_times_to_upsample=2)
            known_face_encoding = face_recognition.face_encodings(image, known_face_locations=face_location)[0]
            case += 1
            writer.writerow([case, folder.split('\\')[-1], *known_face_encoding])
