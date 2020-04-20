# load necessary libraries
import face_recognition, glob

files = glob.glob('../face-recognition/known/*')
known = []


def known_faces():
    for file in files:
        image = face_recognition.load_image_file(file)
        face_location = face_recognition.face_locations(image, number_of_times_to_upsample=2)
        known_face_encoding = face_recognition.face_encodings(image, known_face_locations=face_location)[0]
        known.append(
            {
                "name": file[26:-5],
                "face_encoding": known_face_encoding
            })
    return known
