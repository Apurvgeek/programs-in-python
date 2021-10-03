import numpy as np
import cv2
#from matplotlib import pyplot as plt

#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read the input image
#cap = cv2.VideoCapture(-1)
#ret,img=cap.read()
img = cv2.imread('me.jpeg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3,5,minSize=(30, 30),maxSize=(1000,1000))

# Draw rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,10,147),2)

# Display the output
cv2.imshow('img',img)
cv2.waitKey(2000)
