import numpy as np
from keras import models

# hyperparameters & path
MODELPATH = ('model/')
X_TRAIN = 'dataset/x_train.npy'
Y_TRAIN = 'dataset/y_train.npy'
BATCHSIZE = 64
EPOCHES = 4

# Load trainset
x_train = np.load(X_TRAIN)
y_train = np.load(Y_TRAIN)

# befor loading, run model_set.py
model = models.load_model(MODELPATH)

# Train the model
model.fit(x_train, y_train, batch_size= BATCHSIZE, 
          	epochs= EPOCHES, validation_split=0.1)

# save for later usage
model.save(MODELPATH)