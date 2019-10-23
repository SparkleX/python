import face_recognition
import matplotlib.pyplot as plt
import cv2

image = face_recognition.load_image_file("test.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)
lena = cv2.imread('test.jpg')
for r in face_locations:
    lena = cv2.rectangle(lena, (r[1], r[0]), (r[3], r[2]), (255, 0, 0), 2)
image = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
image = plt.imshow(image)
plt.show()