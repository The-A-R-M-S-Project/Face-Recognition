# import necessary packages
import face_recognition
import PIL.ImageDraw
import PIL.Image
import known

known_faces = known.known_faces()

#loading unknown person's image
unknown = face_recognition.load_image_file('denzel1.jpg')

#detecting unknown person's face location in image
unknown_face_location = face_recognition.face_locations(unknown)[0]

#determining unknown person's face encodings
unknown_face_encoding = face_recognition.face_encodings(unknown)[0]

#Comparing unknown face with known faces to determine match
for known in known_faces:

    # compare = face_recognition.compare_faces([known["face_encoding"]], unknown_face_encoding, tolerance=0.6)[0]
    #drawing images if faces are compatible
    # if compare:
    #     image = PIL.Image.fromarray(unknown)
    #     top, right, bottom, left = unknown_face_location
    #     print("The face pixel location is: Top: {}, Bottom: {}, Left: {}, Right: {}".format(top, bottom, left, right))
    #     draw = PIL.ImageDraw.Draw(image)
    #     draw.rectangle([left, top, right, bottom], outline="green")
    #     draw.text((10, 10), "{}".format(known["name"]), fill=(0, 0, 0))
    #     image.show()
    #     print(compare)

