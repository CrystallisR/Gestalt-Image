import numpy as np
from keras import models
from matplotlib import pyplot as plt

# hyperparameters & path
MODELPATH = ('model/')
DATASET = ('dataset1/')
X_TRAIN = DATASET + 'x_train.npy'
Y_TRAIN = DATASET + 'y_train.npy'
X_TEST = DATASET + 'x_test.npy'
Y_TEST = DATASET + 'y_test.npy'
TLOSS1 = 'visual/loss-type1.png'
TLOSS2 = 'visual/loss-type2.png'
TACC1 = 'visual/accuracy-type1.png'
TACC2 = 'visual/accuracy-type2.png'
TLOSS = TLOSS1
TACC = TACC1
BATCHSIZE = 64
EPOCHES = 50

# Load trainset
X_train = np.load(X_TRAIN)
y_train = np.load(Y_TRAIN)
X_test = np.load(X_TEST)
y_test = np.load(Y_TEST)

# befor loading, run model_set.py
model = models.load_model(MODELPATH)

# Train the model
history = model.fit(X_train, y_train, batch_size= BATCHSIZE, 
          	epochs= EPOCHES, validation_data = (X_test, y_test))

# save for later usage
model.save(MODELPATH)

# visualize
# accuary
fig1 = plt.figure()
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(TLOSS)
# loss
fig2 = plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(TACC)
