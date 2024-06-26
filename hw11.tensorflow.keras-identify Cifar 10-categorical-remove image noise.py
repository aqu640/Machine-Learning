# -*- coding: utf-8 -*-
"""
實作 辨識 Cifar 10 資料集的彩色圖片
使用自編碼器去除圖片雜訊
"""
import numpy as np
import pandas as pd
import keras
from tensorflow.keras.datasets import cifar10

# ==== 數據，切分為訓練和測試集 ====
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(r'x_train.shape = ', x_train.shape)
print(r'y_train.shape = ', y_train.shape)
print(r'x_test.shape = ', x_test.shape)
print(r'y_test.shape = ', y_test.shape)

# print(y_train [0]) # print 標籤資料

# ====  32X32大小的彩色圖片 ====
x_train.shape =  (50000, 32, 32, 3) # 被分成50000張的訓練集
y_train.shape =  (50000, 1) 
x_test.shape =  (10000, 32, 32, 3)  # 被分成10000張的測試集
y_test.shape =  (10000, 1)

channels_first = (60000, 3, 32, 32) #　每個類別有6000張圖片
channels_last = (60000, 32, 32, 3)  # 資料集的shape

# ==== Matplotlib 顯示彩色圖片 ====
import matplotlib.pyplot as plt # pip install matplotlib
from random import randrange

text = ['飛機', '汽車', '鳥' ,'貓', '鹿', '狗', '青蛙', '馬', '船', '卡車']
plt.figure(figsize=(16,10),facecolor='w') # 背景顏色

for i in range(5):
  for j in range(8):
    index = randrange(0, 50000)
    plt.subplot(5, 8, i*8+j+1)
    plt.title("label: {}".format(text[y_train[index][0]]), fontproperties="Microsoft YaHei")
    plt.imshow(x_train[index])
    plt.axis('off')

plt.show()


# ===自編碼器 ==== 
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

from tensorflow.keras.models import Sequential
model = Sequential()


# ====  定義模型 ====
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPool2D

model.add(
    MaxPool2D( # 輸入與輸出是二維數據 提取數據時，保留最大值，去掉其他值
        pool_size = (2, 2) ) )

model.add(
    Conv2D( # 卷積層
        filters = 64,
        kernel_size = (3, 3),
        strides = (1, 1),
        padding = 'same',
        activation = 'relu') )

model.add(
    Flatten() )

model.add(
    Dropout(rate = 0.2) ) # 0.5 對抗過擬合

model.add(Dense( # 全連接層
        units = 10, activation = 'softmax'))

# 需編譯模型轉換成低階 TensorFlow 計算圖
model.compile( # compile 定義損失函數(loss)、優化器(optimizer)、成效衡量指標(mertrics)
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy'])

from tensorflow.keras.callbacks import ModelCheckpoint, CSVLogger, TerminateOnNaN, EarlyStopping

mcp = ModelCheckpoint(filepath='cifar10-{epoch:02d}.h5', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=False, mode='auto', save_freq='epoch')
log = CSVLogger(filename='cifar10.csv', separator=',', append=False)
ton = TerminateOnNaN()
esl = EarlyStopping(monitor='val_loss', patience=7, mode='auto', restore_best_weights=True)
esa = EarlyStopping(monitor='val_accuracy', patience=7, mode='auto', restore_best_weights=True)

from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    shear_range = 0.1,
    rotation_range = 20,
    horizontal_flip = True
)
from sklearn.model_selection import train_test_split
import time
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.1, random_state=int(time.time()))

batch_size = 50
hist = model.fit(
    x = datagen.flow(x_train, y_train, batch_size=batch_size),
    steps_per_epoch = x_train.shape[0] // batch_size,
    epochs = 50,
    validation_data = (x_valid, y_valid),
    callbacks = [mcp, log, ton, esl, esa],
    verbose = 2
)

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
y_predict = model.predict(x_test)
import numpy as np
y_predict = np.argmax(y_predict, axis=1)
y_test = np.argmax(y_test, axis=1)

wrong = np.not_equal(y_predict, y_test)
label = np.arange(*y_test.shape)[wrong]
import pandas as pd
import numpy as np

y_test = np.array(list(map(lambda x: text[x], y_test)))
y_predict = np.array(list(map(lambda x: text[x], y_predict)))
df = pd.DataFrame({'y_Actual': y_test, 'y_Predicted': y_predict})
pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])

history = plt.hist.history
epoch = len(history['loss'])
x = np.arange(epoch)
plt.figure(facecolor='w')
plt.plot(x, history['loss'], label='loss')
plt.plot(x, history['val_loss'], label='val_loss')
plt.plot(x, history['accuracy'], label='accuracy')
plt.plot(x, history['val_accuracy'], label='val_accuracy')

plt.xlim(0, epoch-1)
plt.xticks([i for i in range(0,epoch,epoch//5)],[str(i) for i in range(0,epoch,epoch//5)])
plt.xlabel('epoch')
plt.ylim(0,1)
plt.ylabel('acc-loss')
plt.legend()
plt.show()

model.summary() # 顯示模型摘要
# 訓練模型
from tensorflow.keras.datasets import mnist
from tensorflow.keras.datasets import Model
from tensorflow.keras.datasets import Dense, Input
seed=7
np.random.seed (seed)
(X_train_),( X_test,_)= mnist.load_data()




