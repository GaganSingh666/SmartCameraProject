
import time
import cv2
import requests
from motorLogic import *
'''
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

cv2.imshow("Image", image)
cv2.waitKey(0)

'''

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
something, anything = "Something","Anything" #change to any variable type or string that you want, upto three values can be sent in params
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    print(faces)
    print(type(faces))
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('cap', img)
    if(type(faces)!= tuple):
        print('face detected')
        r=requests.post("https://maker.ifttt.com/trigger/face_detected/with/key/cRwNyLtZdhwnCdOte4rW3cyjc9qqvvMSSUkoOnFH1J4")
        #wait sometime so that multiple triggers are not sent immediately to webhook. also Time to move out of frame otherwise camera will spam webhook with emails as long as face is in view.
        time.sleep(15) #
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
    if cv2.waitKey(33) == ord('w'):
        moveUp()
        
    if cv2.waitKey(33) == ord('s'):
        moveDown()
    if cv2.waitKey(33) == ord('a'):
        moveLeft()
    if cv2.waitKey(33) == ord('d'):
        #time.sleep(1)
        moveRight()
        #time.sleep(5)
cap.release()
cv2.destroyAllWindows()