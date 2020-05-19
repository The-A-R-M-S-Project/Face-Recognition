import face_recognition
import PIL.Image
import PIL.ImageDraw

image = face_recognition.load_image_file('rodrick.jpg')

face_location = face_recognition.face_locations(image)[0]

p_image = PIL.Image.fromarray(image)
top, right, bottom, left = face_location
print("The face pixel location is: Top: {}, Bottom: {}, Left: {}, Right: {}".format(top, bottom, left, right))
draw = PIL.ImageDraw.Draw(p_image)
draw.rectangle([left, top, right, bottom], outline="green", width=2)

p_image.show()