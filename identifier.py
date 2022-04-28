import os
import sys
import cv2

directory = sys.argv[1]
choice = sys.argv[2]


stop_signs = cv2.CascadeClassifier('../stop_data.xml')
faces = cv2.CascadeClassifier('../haarcascade_frontalface.xml')

files = []

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        files.append(filename)

if directory == "../faces":
    for file in files:
        img = cv2.imread(directory + "/" + file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = faces.detectMultiScale(img_gray, 1.1, 4)
        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        cv2.imshow('img', img)
        cv2.waitKey()

elif directory == "../stop_data":
    for file in files:
        print(file)
        img = cv2.imread(directory + "/" + file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = stop_signs.detectMultiScale(img_gray, 1.05, minNeighbors=0)
        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        cv2.imshow('img', img)
        cv2.waitKey()

else:
    for file in files:
        if choice == 'a':
            img = cv2.imread(directory + "/" + file)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            objects = faces.detectMultiScale(img_gray, 1.1, 4)
            for (x, y, w, h) in objects:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display the output
            cv2.imshow('img', img)
            cv2.waitKey()
        elif choice == 'b':
            img = cv2.imread(directory + "/" + file)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            objects = stop_signs.detectMultiScale(img_gray, minSize =(20, 20))
            for (x, y, w, h) in objects:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display the output
            cv2.imshow('img', img)
            cv2.waitKey()