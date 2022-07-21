# CrystallisR 2022
import cv2
import numpy as np
import os
from keras.utils import to_categorical

def readImgsAsMatrix(folder):
    '''
    read all images in a folder and save into a matrix
    '''
    matrix = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), 0)
        if img is not None: matrix.append(img)
    return np.array(matrix)

def trainTestSplit(data, rate=0.8):
    '''
    split data into train set and test set
    '''
    brk = int(len(data)*rate)
    return data[:brk], data[brk:]

def unisonShuffledCopies(a, b):
    '''
    shuffle 2 arrays with correspondence relation reserved
    '''
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def loadData(folders):
    '''
    load data for a n-ary classifier
    
    parameter
    ---------
    folders: list of folders (path)
    '''
    X_data = readImgsAsMatrix(folders[0])
    y_data = np.full((len(X_data), 1), 0)
    for i in range(1, len(folders)):
        X_data_i = readImgsAsMatrix(folders[i])
        X_data = np.concatenate((X_data, X_data_i), axis=0)
        y_data_i = np.full((len(X_data_i), 1), i)
        y_data = np.concatenate((y_data, y_data_i), axis=0)
    X_data, y_data = unisonShuffledCopies(X_data, y_data)
    X_train, X_test = trainTestSplit(X_data)
    y_train, y_test = trainTestSplit(y_data)
    return (X_train, y_train), (X_test, y_test)

def process(folders, classes, x_train_p, x_test_p, y_train_p, y_test_p):
    # load data
    (x_train, y_train), (x_test, y_test) = loadData(folders)
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
        
