import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
import cv2 as cv
import sys

class_names = ['angry', 'happy', 'normal', 'sad', 'suprise']

model = load_model('model.h5')
model.load_weights('model_checkpoint.h5')

cap=cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv.resize(frame, dsize=None, fx=0.5, fy=0.5)
    img = frame.copy()
    img = cv.resize(img, (128, 128))
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    img = img.astype('float')/255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    print("This picture is: ", class_names[np.argmax(pred[0])], (pred[0]))
    print(np.max(pred[0], axis=0))
    if (np.max(pred) >= 0.8) and (np.argmax(pred[0]) != 0):
        font = cv.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1.5
        color = (0, 255, 0)
        thickness = 2
        cv.putText(frame, class_names[np.argmax(pred)], org, font,
                    fontScale, color, thickness, cv.LINE_AA)
    cv.imshow("Picture", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()