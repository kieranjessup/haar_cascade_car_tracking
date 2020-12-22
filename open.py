# open.py

import cv2
import numpy as np

# source footage
#cap = cv2.VideoCapture('')
cap = cv2.VideoCapture('traffic.mp4')


# pre-trained classifier
car_classifier_file = 'car.xml'

# create classifier
car_tracking = cv2.CascadeClassifier(car_classifier_file)

# run until all source stops
while True:

    # read the current frame
    (read_successful, frame) = cap.read()

    # safe coding
    if read_successful:
        # convert to grayscale for HAAR
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars and pedestrians
    cars = car_tracking.detectMultiScale(grayscaled_frame)
    
    # draw rectangle around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow('lol', frame)

    # stop auto-close
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
