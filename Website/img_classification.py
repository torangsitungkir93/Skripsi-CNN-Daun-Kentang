import keras
import cv2
from PIL import Image, ImageOps
import numpy as np


def teachable_machine_classification(img, weights_file):

    model = keras.models.load_model(weights_file)
    image = img
    size = (256, 256)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = np.asarray(image)
    image = np.expand_dims(image, axis=0)
    image = image/255
    prediction = model.predict(image)
    return np.argmax(prediction)


def probabilitas(img, weights_file):

    model = keras.models.load_model(weights_file)
    image = img
    size = (256, 256)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = np.asarray(image)
    image = np.expand_dims(image, axis=0)
    image = image/255
    preds = model.predict(image)
    hasil_label = np.argmax(preds)
    hasil_prob = "{:.2f}".format(100 * np.max(preds))
    preds_array = np.around(preds, 3)
    return preds_array, hasil_prob
