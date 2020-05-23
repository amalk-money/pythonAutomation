from keras.datasets import mnist

dataset = mnist.load_data('mymnist.db')

train, test = dataset

x_train, y_train = train

x_test, y_test = test

from keras.utils.np_utils import to_categorical

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

import numpy as np

X_train_1D = x_train.reshape(x_train.shape[0],x_train[0].shape[0],x_train[0].shape[1],1)
X_test_1D = x_test.reshape(x_test.shape[0],x_test[0].shape[0],x_test[0].shape[1],1)

x_train = X_train_1D.astype('float32')

x_test = X_test_1D.astype('float32')

from keras.layers import Convolution2D

from keras.layers import MaxPooling2D

from keras.layers import Flatten

from keras.layers import Dense

from keras.models import Sequential

model = Sequential()

model.add(Convolution2D(filters=32,kernel_size=(19,19),activation='relu',input_shape=(28, 28, 1)))

model.add(MaxPooling2D(pool_size=(6,6)))

model.add(Flatten())

model.add(Dense(units=150, activation='relu'))

#add

model.add(Dense(units=10, activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train,y_train,epochs=1,validation_data=(x_test, y_test),shuffle=True)
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
