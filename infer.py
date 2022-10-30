# from matplotlib.pyplot import imshow
from tensorflow.keras.models import load_model
import os
import numpy as np
from PIL import Image

model = load_model('traffic_signal_classifier.h5')

img_path = "test2/image.jpg"
im = Image.open(img_path)
im = im.resize((30, 30))
im = np.asarray(im.getdata()).reshape((30, 30, 3))
output = np.argmax(model.predict(np.expand_dims(im, axis=0)))

map = {
    0: 20,
    1: 30,
    2: 50,
    3: 60,
    4: 70,
    5: 80,
    6: 80,
    7: 100,
    8: 120
}

speeds = -1 if output not in map else map[output]
# print(speeds)

# print(f"Speed limit is {speed}" if speed != -1 else "No speed limit")
exit(speeds)
