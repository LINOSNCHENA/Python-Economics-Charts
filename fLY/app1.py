from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Dropout, Flatten, Dense
import numpy as np

X_train = np.random.rand(200,128,128,3)
y_train = np.random.rand(200,2)
X_test = np.random.rand(10,128,128,3)
y_test = np.random.rand(10,2)

rounds=10
model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc' ,'mse'])
history = model.fit(X_train, y_train, epochs=rounds, validation_data=(X_test,y_test))


print('')
print("============================|Testing_One2|=======")
scores = model.evaluate(X_test, y_test, verbose=1)    
test = model.evaluate(X_test, y_test, verbose=1)
print("zed = "+"%s: %.2f%%" % (model.metrics_names[2], scores[2]*100))
cvscores = []
cvscores.append(scores[1] * 100)
accuracy1 = model.evaluate(X_test, y_test)
print("Model-Loss1, Model-MSE2, Model-Accuracy3", accuracy1)
print("============================|Testing_One2|=======")
print('')


print("============================|Plane_One2|=======")

print(history.history.keys())
print(history.history)

plt.figure(figsize=(18,10))
plt.plot(history.history['acc'],color="green")
plt.plot(history.history['val_acc'],color="red")
plt.title('Random-Data-Model-Accuracy-10.A')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.legend(['train1', 'validation1'], loc='best')
plt.savefig('../UXViews/10BB1.png')
plt.show()

plt.figure(figsize=(18,10))
plt.plot(history.history['mse'], color="green")
plt.plot(history.history['val_mse'], color="blue")
plt.title('Random-Data-Model-Accuracy-10.B')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.grid(True)
plt.legend(['train2', 'validation2'], loc='best')
plt.savefig('../UXViews/10BB2.png')
plt.show()

plt.figure(figsize=(18,10))
plt.plot(history.history['loss'],color="green")
plt.plot(history.history['val_loss'],color="fuchsia")
plt.title('Random-Data-Model-Accuracy-10.C')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.legend(['train3', 'validation3'], loc='best')
plt.savefig('../UXViews/10BB3.png')
plt.show()

print("=============================|Plane_One2|=======")

# I expect that X_train to be shape (n_samples,128,128,3) and y_train to be shape (n_samples,2)
##32/32+10/10