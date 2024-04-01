import pandas as pd #導入pandas函數
import numpy as np#導入numpy函數
from keras.models import Sequential
from keras.layers import Dense


# ==== 1.資料預處理 ====
df = pd.read_csv('./diabetes.csv')
print(df.head())
print(df.shape)

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:8]
Y = dataset[:, 8]

model = Sequential() #　建立model
model.add(Dense(10,input_shape=(8,),activation="relu"))  #呼叫add()
model.add(Dense(8,activation="relu")) # 啟動函數 ReLU函數
model.add(Dense(1, activation="softmax")) # 啟動函數 Sigmoid函數
model.summary()

# ==== 3.編譯模型 ====
model.compile(loss="binary_crossentropy",
optimizer="sgd", metrics=["accuracy"])

# ==== 4.訓練模型 ====
model.fit(X, Y, epochs=150, batch_size=10)

# ==== 5.評估模型 ====
loss, accuracy = model.evaluate(X, Y)
print("準確度 = {:.2f}".format(accuracy))





import matplotlib.pyplot as plt
from keras.utils import to_categorical



# ==== 標準化提升準確度 ====
X -= X.mean(axis=0) # 述特徵資料X 減掉mean()平均值
X /= X.std(axis=0)  # 除std()標準差
Y = to_categorical(Y)

# ==== 繪出訓練&驗證損失的趨勢表 ====
epochs = range(1, len(loss)+1)
plt.plot(epochs, loss, "bo", label="Training Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
