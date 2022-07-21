# CrystallisR 2022
from tools import process

# save/load path data
FOLDERP1 = ("positive_t1")
FOLDERN1 = ("negative_t1")
FOLDERP2 = ("positive_t2")
FOLDERN2 = ("negative_t2")

X_TRAIN = 'datasetMul/x_train.npy'
Y_TRAIN = 'datasetMul/y_train.npy'
X_TEST = 'datasetMul/x_test.npy'
Y_TEST = 'datasetMul/y_test.npy'

X_TRAIN1 = 'dataset/x_train.npy'
Y_TRAIN1 = 'dataset/y_train.npy'
X_TEST1 = 'dataset/x_test.npy'
Y_TEST1 = 'dataset/y_test.npy'

X_TRAIN2 = 'dataset2/x_train.npy'
Y_TRAIN2 = 'dataset2/y_train.npy'
X_TEST2 = 'dataset2/x_test.npy'
Y_TEST2 = 'dataset2/y_test.npy'

'''
# train type-2
CLASSES = 2
folders = [FOLDERP2, FOLDERN2]
process(folders, CLASSES, X_TRAIN2, X_TEST2, Y_TRAIN2, Y_TEST2)
'''

# train all type
CLASSES = 3
folders = [FOLDERP1, FOLDERN1, FOLDERN2]
process(folders, CLASSES, X_TRAIN, X_TEST, Y_TRAIN, Y_TEST)