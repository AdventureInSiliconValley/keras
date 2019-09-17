from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# Crating another branch!
model.compile(loss='categorial_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])