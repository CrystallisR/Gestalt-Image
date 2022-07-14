import cv2
import numpy as np
import os

def readImgsAsMatrix(folder):
    matrix = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), 0)
        if img is not None: matrix.append(img)
    return np.array(matrix)

def trainTestSplit(data, rate=0.8):
    brk = int(len(data)*rate)
    return data[:brk], data[brk:]

def unisonShuffledCopies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def loadData(pos_folder, neg_folder):
    X_pos = readImgsAsMatrix(pos_folder)
    X_neg = readImgsAsMatrix(neg_folder)
    y_pos = np.ones(len(X_pos), dtype=np.uintc)
    y_neg = np.zeros(len(X_neg), dtype=np.uintc)
    X_data = np.concatenate((X_pos, X_neg), axis=0)
    y_data = np.concatenate((y_pos, y_neg), axis=0)
    X_data, y_data = unisonShuffledCopies(X_data, y_data)
    X_train, X_test = trainTestSplit(X_data)
    y_train, y_test = trainTestSplit(y_data)
    return (X_train, y_train), (X_test, y_test)
        
