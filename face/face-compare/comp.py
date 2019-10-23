import face_recognition

for i in range(0,7):
    for j in range(0,7):
        if i<j :
            picture_of_me = face_recognition.load_image_file(str(i)+".jpg")
            my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
            unknown_picture = face_recognition.load_image_file(str(j)+".jpg")
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
            print(i,j,results[0])

