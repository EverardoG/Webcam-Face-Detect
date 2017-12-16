import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import serial
import time

"""This initiates the arduino"""
arduino = serial.Serial("/dev/ttyACM0",9600, timeout =5);
time.sleep(1)
print("Starting up Arduino")
test_arduino = 1
arduino.flush()


"""This is all face cascade stuff"""

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

"""Here it sets up a video stream and intializes how many faces there are to 0"""

video_capture = cv2.VideoCapture(1)
anterior = 0

"""This is all the code for scanning for faces"""

while True:

    happiness_index = 0
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
        )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    n0=anterior

    #print("First one:",n0)

    if anterior != len(faces):
        anterior = len(faces)

        nf=anterior
        #tf = dt.datetime.now()
        #print("Second one:",nf)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
        #print(dt.datetime.now())



        if nf > n0:
            happiness_index = 1
            print("Happy! :D")

        if nf < n0:
            happiness_index = 2
            print("Sadness :(")

    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
