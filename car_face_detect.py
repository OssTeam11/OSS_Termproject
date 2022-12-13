import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0 :
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x, y, w, h) in faces :
        if(200 < w) :
            print("Too Close! Stop Car")
        elif(100 < w) : 
            print("Slow Down a car")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Camera", frame)

cap.release()
cv2.destroyAllWindows()