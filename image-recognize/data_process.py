import numpy as np
from keras.utils import to_categorical
from keras.datasets import mnist
import cv2
import os
import numpy as np
from tools import loadData

# save/load path data
FOLDER1 = ("positive_t1")
FOLDER2 = ("negative_t1")
X_TRAIN = 'dataset/x_train.npy'
Y_TRAIN = 'dataset/y_train.npy'
X_TEST = 'dataset/x_test.npy'
Y_TEST = 'dataset/y_test.npy'
# divide data into 2 categories
CLASSES = 2

# load MNIST handwritten digit trainset
(x_train, y_train), (x_test, y_test) = loadData(FOLDER1, FOLDER2)
print(type(y_train[0]))

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
# convert class vectors to binary class matrices
y_train = to_categorical(y_train, CLASSES)
y_test = to_categorical(y_test, CLASSES)

# status
print("train set:")
print(x_train.shape)
print(type(x_train))
print(y_train.shape)
print(type(y_train))
print("test set:")
print(x_test.shape)
print(type(x_test))
print(y_test.shape)
print(type(y_test))

np.save(X_TRAIN, x_train)
np.save(X_TEST, x_test)
np.save(Y_TRAIN, y_train)
np.save(Y_TEST, y_test)

print("Data preprocessing finished")