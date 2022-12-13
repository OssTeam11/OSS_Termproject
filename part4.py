for(x, y, w, h) in faces :
        if(200 < w) :
            print("Too Close! Stop Car")
        elif(100 < w) : 
            print("Slow Down a car")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)