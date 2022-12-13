import cv2

cap = cv2.VideoCapture(0)

while(True):
    retval, frame = cap.read()
    
    if retval == False:
        break
    cv2.imshow('frame', frame)

    # 30초가 지나거나, ESC 키가 입력되면 while 반복문 종료
    if cv2.waitKey(30) == 27:
        break

cap.release()

cv2.destroyAllWindows()