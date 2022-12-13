import cv2

while cv2.waitKey(33) < 0 :
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)