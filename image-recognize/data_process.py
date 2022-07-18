import numpy as np
from keras.utils import to_categorical
from keras.datasets import mnist
import cv2
import os
import numpy as np
from tools import loadData

# save/load path data
FOLDERP1 = ("positive_t1")
FOLDERN1 = ("negative_t1")
FOLDERP2 = ("positive_t2")
FOLDERN2 = ("negative_t2")
X_TRAIN1 = 'dataset/x_train.npy'
Y_TRAIN1 = 'dataset/y_train.npy'
X_TEST1 = 'dataset/x_test.npy'
Y_TEST1 = 'dataset/y_test.npy'
X_TRAIN2 = 'dataset2/x_train.npy'
Y_TRAIN2 = 'dataset2/y_train.npy'
X_TEST2 = 'dataset2/x_test.npy'
Y_TEST2 = 'dataset2/y_test.npy'
# divide data into 2 categories
CLASSES = 2

def process(folder1, folder2, classes, x_train_p, x_test_p, y_train_p, y_test_p):
    # load data
    (x_train, y_train), (x_test, y_test) = loadData(folder1, folder2)
    # Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255
    # Make sure images have shape (28, 28, 1)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    # convert class vectors to binary class matrices
    y_train = to_categorical(y_train, classes)
    y_test = to_categorical(y_test, classes)
    # show status
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
    # save data
    np.save(x_train_p, x_train)
    np.save(x_test_p, x_test)
    np.save(y_train_p, y_train)
    np.save(y_test_p, y_test)
    print("Data preprocessing finished")
    
process(FOLDERP2, FOLDERN2, CLASSES, X_TRAIN2, X_TEST2, Y_TRAIN2, Y_TEST2)