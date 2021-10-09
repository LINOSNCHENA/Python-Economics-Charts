## DATA SCIENCE AND TITANIC

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ===========================================================================================================

data = pd.read_csv('../datain/titanicData.csv')
data.replace('?', np.nan, inplace= True)
data = data.astype({"age": np.float64, "fare": np.float64})

fig, axs = plt.subplots(ncols=5, figsize=(18,8))
sns.violinplot(x="survived", y="age", hue="sex", data=data, ax=axs[0])
plt.title("Survivals and dead1")
sns.pointplot(x="sibsp", y="survived", hue="sex", data=data, ax=axs[1])
sns.pointplot(x="parch", y="survived", hue="sex", data=data, ax=axs[2])
sns.pointplot(x="pclass", y="survived", hue="sex", data=data, ax=axs[3])
sns.violinplot(x="survived", y="fare", hue="sex", data=data, ax=axs[4])
plt.suptitle('Five plots of dead vs survived -1.1',  fontsize=20, fontweight="bold", color='g')
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('../UXviews/Titanic1.png')
plt.show()

# 1. FIVE CATEGORIS

x1=data.columns
x2=pd.value_counts(data.values.flatten())

# 2. COMPARISSON OF PLOT AND PRINT DATA 14 fields
data.replace({'male': 1, 'female': 0}, inplace=True)
data.corr().abs()[["survived"]]
data.plot(figsize=(16, 8))
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.suptitle('Comparing using five different views: dead vs survived -1.2',  fontsize=20, fontweight="bold", color='g')
plt.tight_layout()
plt.savefig('../UXviews/Titanic2.png')
plt.show()
plt.clf();plt.close()
print(data)

# 3. Cleaning and creating 7th fields 
data['relatives'] = data.apply (lambda row: int((row['sibsp'] + row['parch']) > 0), axis=1)
data.corr().abs()[["survived"]]
data = data[['sex', 'pclass','age','relatives','fare','survived']].dropna()
data.plot(figsize=(16, 8))
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.suptitle('general comparisons plots of dead vs survived -1.3',  fontsize=20, fontweight="bold", color='g')
plt.tight_layout()
plt.savefig('../UXviews/Titanic3.png')
plt.show()
print(data)

# 4. AI-Machine Learning algorithm-TRAIN AND EVALUATE OF SEVEN FEATURES
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data[['sex','pclass','age','relatives','fare']],
 data.survived, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)
from sklearn import metrics
predict_test = model.predict(X_test)
print(metrics.accuracy_score(y_test, predict_test))

# =============================================================================================
# 5. AI-ModelSkLearn-Artificial-Neural-Networks-TRAIN AND EVALUATE OF SEVEN FEATURES
from keras.models import Sequential
from keras.layers import Dense
roundCycles=11
model2 = Sequential()
model2.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu', input_dim = 5))
model2.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu'))
model2.add(Dense(1, kernel_initializer = 'uniform', activation = 'sigmoid'))
model2.summary()
model2.compile(optimizer="adam", loss='binary_crossentropy', metrics=['mse','acc','accuracy'])
history = model2.fit(X_train, y_train, validation_split=0.33,epochs=roundCycles, batch_size=4, verbose=2)
model2.fit(X_train, y_train, batch_size=4,validation_split=0.33,epochs=roundCycles)


# ==================================================================================================

print('=================| 1. ModelSkLearn  Vs 2. ModelKeras|===================')
y_pred=(model.predict(X_test) > 0.5).astype("int32") ## Binary and Sigmond-last
y_pred2=(model2.predict(X_test) > 0.5).astype("int32") ## Binary and Sigmond-last
ModelKeras=(metrics.accuracy_score(y_test, y_pred))
ModelSkLearn=(metrics.accuracy_score(y_test, y_pred2))


print("SIZED1 = : ==============================|AAAAAAAAAAAAAAA")
print(len(y_pred))
print(y_pred.reshape(1,-1))
print("SIZED2 = : ==============================|BBBBBBBBBBBBBBBB")
print(len(y_pred2))
print(y_pred2.reshape(1,-1))

print('==================Keras============================')
print(ModelKeras)
print('==================SkyLearn=========================')
print(ModelSkLearn)
print('==================Balance==========================')
print(ModelKeras-ModelSkLearn)

print('=================| 1. ModelSkLearn  Vs 2. ModelKeras|===================')
## 6. PLOTTING
print(history.history)
plt.figure(figsize=(18, 9))
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Accuracy - Training and Testing in fever plot #4 KAFUE',fontsize=20, fontweight="bold", color='g')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.legend(['Acc_Training Data', 'Acc_Validation data'], loc='best')
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('../UXviews/Titanic4.png')
plt.show()

# plot metrics from trained model	//	# summarize history for loss 	# 2
plt.figure(figsize=(18, 9))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss - Training and testing loss in fever plot #5 KAFUE',fontsize=20, fontweight="bold", color='g')
plt.ylabel('Loss values')
plt.xlabel('epoch')
plt.legend(['Loss_Training Data', 'Loss_Validation data'], loc='best')
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('../UXviews/Titanic5.png')
plt.show()

# plot metrics from trained //	# summarize history for mean_squared_error # 3
plt.figure(figsize=(18, 9))
plt.plot(history.history['mse'])
plt.plot(history.history['val_mse'])
plt.title('MSE - Training and testing in fever plot #6 KAFUE',fontsize=20, fontweight="bold", color='g')
plt.ylabel('mean_squared_error values')
plt.xlabel('epoch')
plt.legend(['MSE_Training Data', 'MSE_Validation data'], loc='best')
plt.xticks(rotation=20)
plt.yticks(rotation=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('../UXviews/Titanic6.png')
plt.show()

print('=======================|Titanic Sank at P120|==============================')
