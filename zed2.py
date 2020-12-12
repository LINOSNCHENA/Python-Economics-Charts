## DATA SCIENCE AND TITANIC

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/tdata.csv')
data.replace('?', np.nan, inplace= True)
data = data.astype({"age": np.float64, "fare": np.float64})

fig, axs = plt.subplots(ncols=5, figsize=(30,5))
sns.violinplot(x="survived", y="age", hue="sex", data=data, ax=axs[0])
sns.pointplot(x="sibsp", y="survived", hue="sex", data=data, ax=axs[1])
sns.pointplot(x="parch", y="survived", hue="sex", data=data, ax=axs[2])
sns.pointplot(x="pclass", y="survived", hue="sex", data=data, ax=axs[3])
sns.violinplot(x="survived", y="fare", hue="sex", data=data, ax=axs[4])

# 1. FIVE CATEGORIS
#print(axs)
# for row in data.iterrows():
#     print (row)
# plt.show()
x1=data.columns
x2=pd.value_counts(data.values.flatten())
# print(x1)
# print(x2)
# x2.plot()

# 2. COMPARISSON OF PLOT AND PRINT DATA 14 fields
data.replace({'male': 1, 'female': 0}, inplace=True)
data.corr().abs()[["survived"]]
data.plot()
plt.show()
plt.clf();plt.close()
print(data)

# 3. Cleaning and creating 7th fields 
data['relatives'] = data.apply (lambda row: int((row['sibsp'] + row['parch']) > 0), axis=1)
data.corr().abs()[["survived"]]
data = data[['sex', 'pclass','age','relatives','fare','survived']].dropna()
data.plot()
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


# 5. AI-ANN-Artificial-Neural-Networks-TRAIN AND EVALUATE OF SEVEN FEATURES
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu', input_dim = 5))
model.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(1, kernel_initializer = 'uniform', activation = 'sigmoid'))

model.summary()

model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=32, epochs=50)

y_pred = model.predict_classes(X_test)
print()
print('MACHINE LEARNING THEN ARTIFICIAL NEURAL NETWORK RESULTS)')
print('==============================================')
print()
ML=(metrics.accuracy_score(y_test, y_pred))
ANN=(metrics.accuracy_score(y_test, predict_test))
print(ML)
print(ANN)
print(ML-ANN)
print('================= THE END -===================')
print()
print('==============================================')
print()
