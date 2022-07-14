from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Input, Dropout
from keras.models import Sequential

# hyperparameters & path
MODELPATH = ('model/')
SHAPE = (128, 128, 1)
CLASSES = 2

# Set Neural Network model - SBNet
model = Sequential(
    [
        Input(shape=SHAPE),
        Conv2D(128, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, kernel_size=(5, 5), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(32, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        BatchNormalization(),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(CLASSES, activation="softmax"),
    ],
    name= "SBNet"
)

model.summary()

model.compile(loss='categorical_crossentropy', 
	    	optimizer='adam',
	      	metrics=['acc'])

# save for later usage
model.save(MODELPATH)