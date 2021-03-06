import numpy as np
from keras import models

# hyperparameters & path
MODELPATH = ('model/')
DATASET = ('dataset2/')
X_TEST = DATASET + 'x_test.npy'
Y_TEST = DATASET + 'y_test.npy'

# Load testset
x_test = np.load(X_TEST)
y_test = np.load(Y_TEST)

# load trained model
model = models.load_model(MODELPATH)

score = model.evaluate(x_test, y_test, verbose = True) 

print('Test loss:', score[0]) 
print('Test accuracy:', score[1])