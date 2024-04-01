# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:54:36 2023

@author: r
"""

import numpy as np                   


# ====使用Pandas　載入csv資料集 ====
import pandas as pd
df = pd.read_csv('diabetes.csv')
# print(df.head())
print("(幾筆記錄, 幾個欄位)=\n",df.shape)

# ==== 1.資料預處理 ====
df = pd.read_csv("./diabetes.csv")
dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:8]
Y = dataset[:, 8]

# ==== 2.定義模型 ====
from keras.models import Sequential
from keras.layers import Dense

model = Sequential() #　建立model
model.add(Dense(10,input_shape=(8,),activation="relu"))  #　呼叫add()
model.add(Dense(10,input_shape=(8,),activation="relu"))
model.add(Dense(8, activation="relu"))    # 啟動函數 ReLU函數
model.add(Dense(1, activation="sigmoid")) # 啟動函數 Sigmoid函數
model.summary()

# ==== 3.編譯模型 ====
model.compile(loss="binary_crossentropy",
optimizer="sgd", metrics=["accuracy"])

# ==== 4.訓練模型 ====
model.fit(X, Y, epochs=10, batch_size=10)

# ==== 5.評估模型 ====
loss, accuracy = model.evaluate(X, Y)
print("準確度 = {:.2f}".format(accuracy))

# ==== 標準化提升準確度 ====
X -= X.mean(axis=0) # 述特徵資料X 減掉mean()平均值
X /= X.std(axis=0)  # 除std()標準差

# ==== 在輸出層使用softmax啟動函數 ====
from keras.utils import to_categorical
Y = to_categorical(Y)

# ==== 第2層隱藏層 修改神經網路的輸出層 ====
# model = Sequential()
# model.add(Dense(10, input_shape=(8,), 
# activation="relu"))
# model.add(Dense(1, activation="relu"))
# model.add(Dense(2, activation="softmax"))

# # 在Dense神經層 新增初始權重矩陣&偏向量
model = Sequential()
model.add(Dense(10, input_shape=(8,), 
kernel_initializer="random_uniform", bias_initializer="ones", 
activation="relu"))
model.add(Dense(6, kernel_initializer="random_uniform", 
bias_initializer="ones", activation="relu"))
model.add(Dense(2, kernel_initializer="random_uniform", 
bias_initializer="ones", activation="softmax"))

# ==== 編譯模型使用adam優化器 ====
model.compile(loss="binary_crossentropy", 
optimizer="adam", metrics=["accuracy"])

# ==== 資料集分割成 訓練&測試 ====
X_train, Y_train = X[:690], Y[:690] 
X_test, Y_test = X[690:], Y[690:]

model.fit(X_train, Y_train, epochs=10,
batch_size=10, verbose=0)

loss, accuracy = model.evaluate(X_train, Y_train)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))

loss, accuracy = model.evaluate(X_test, Y_test)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# ==== 手動分割 ====
history = model.fit(X_train, Y_train, validation_data
= (X_test, Y_test), epochs = 10, batch_size=10)

# ==== 繪出訓練&驗證損失的趨勢表 ====
import matplotlib.pyplot as plt
acc = history.history["acc"] # acc訓練準確度
epochs = range(1, len(acc)+1)
val_acc = history.history["val_acc"] # val_acc 驗證準確度
plt.plot(epochs, acc, "b-", label="Training Acc")
plt.plot(epochs, val_acc, "r--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()








