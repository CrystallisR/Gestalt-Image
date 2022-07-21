# CrystallisR 2022
from tools import process

# save/load path data
FOLDERP1 = ("positive_t1")
FOLDERN1 = ("negative_t1")
FOLDERP2 = ("positive_t2")
FOLDERN2 = ("negative_t2")
FOLDERP3 = ("positive_t3")
FOLDERN3 = ("negative_t3")

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

X_TRAIN3 = 'dataset3/x_train.npy'
Y_TRAIN3 = 'dataset3/y_train.npy'
X_TEST3 = 'dataset3/x_test.npy'
Y_TEST3 = 'dataset3/y_test.npy'

'''
# train type-1
CLASSES1 = 2
folders1 = [FOLDERP1, FOLDERN1]
process(folders1, CLASSES1, X_TRAIN1, X_TEST1, Y_TRAIN1, Y_TEST1)
'''

'''
# train type-2
CLASSES2 = 2
folders2 = [FOLDERP2, FOLDERN2]
process(folders, CLASSES2, X_TRAIN2, X_TEST2, Y_TRAIN2, Y_TEST2)
'''
'''
# train type-3
CLASSES3 = 2
folders3 = [FOLDERP3, FOLDERN3]
process(folders3, CLASSES3, X_TRAIN3, X_TEST3, Y_TRAIN3, Y_TEST3)
'''


# train all type
CLASSESA = 5
foldersa = [FOLDERP1, FOLDERN1, FOLDERN2, FOLDERP3, FOLDERN3]
process(foldersa, CLASSESA, X_TRAIN, X_TEST, Y_TRAIN, Y_TEST)


