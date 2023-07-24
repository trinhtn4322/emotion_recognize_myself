import cv2 as cv
import os

cap=cv.VideoCapture(0)
label_folder = 'suprise'
# change label in list : ['happy','angry','sad','normal','suprise']
i=0
while(True):
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv.resize(frame, dsize=None, fx=1, fy=1)
    cv.imshow('Camera',frame)
    if i >= 60 and i<=3060:
        print('Number of pictures = ',i-60)
        cv.imwrite('data/' + str(label_folder) + '/' + str(i) + '.png',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
