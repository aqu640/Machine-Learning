"""
# 機器學習 HW5-3

用店面面積 和 車站距離
來預測單月營業額
pip install scikit-learn
"""
# ====  導入繪圖套件  ====
import matplotlib.pyplot as plt

# ====   Python 數據處理套件  ====
import pandas as pd 
import numpy as np

# ====  導入迴歸模型套件  ====
from sklearn.linear_model import LinearRegression

# ==== 建立身高體重與腰圍的 Numpy 陣列 ====
A = np.array([10, 8, 8, 5, 7, 8, 7, 9, 6, 9])  # 店面面積
                   
D = np.array ([80, 0, 200, 200, 300, 230, 40, 0, 330, 180]) # 車站距離

I = np.array([49.6, 36.6, 37.1, 20.8, 24.6, 29.7, 36.6, 43.6, 19.8, 36.4]) # 單月營業額


# ==== 建立一個線性迴歸模型 ====
lm = LinearRegression()
lm.fit (np.reshape(A,  (len(A), 1)), # 將資料放進模型內訓練
           np.reshape(I, (len(I), 1)))

# ==== 預測 ====
print("依序由店面面積預測營業額，再由車站距離預測營業額\n")
print("店面面積 & 車站距離不為負值\n")
m = float(input("輸入店面面積:  ")) # Element you want to input 可以輸入小數點

if  m >= 0 :
    to_be_predicted1 = np.array([m])           
    predicted_1 = lm.predict(np.reshape(to_be_predicted1, (len(to_be_predicted1), 1)))

    w0 = lm.coef_         # 斜率係數
    w1 = lm.intercept_ # 截距
    # y =  w_1x + w_0

    # ==== 繪圖 ====
    plt.scatter(A, I, color='black')
    plt.plot(A, lm.predict(np.reshape(A, (len(A), 1))), color='blue', linewidth=3)
    plt.plot(to_be_predicted1, predicted_1, color = 'red', marker = '^', markersize = 10)

    plt.xlabel("Area (cm)", fontweight = "bold")   # 設定x座標標題及粗體
    plt.ylabel("Income (kg)", fontweight = "bold")   # 設定y座標標題及粗體
    plt.show()

    # ==== 建立一個線性迴歸模型 ====
    lm = LinearRegression()
    lm.fit (np.reshape(D,  (len(D), 1)), # 將資料放進模型內訓練
           np.reshape(I, (len(I), 1)))
else:
    print("店面面積需大於0")
         
# ==== 預測 ====
n = float(input("輸入車站距離:  ")) # Element you want to input 可以輸入小數點
if  n >= 0 :
    to_be_predicted_x = np.array([n])           
    predicted_y = lm.predict(np.reshape(to_be_predicted_x, (len(to_be_predicted_x), 1)))
    w0 = lm.coef_         # 斜率係數
    w1 = lm.intercept_ # 截距
    # y =  w_1x + w_0

    # ==== 繪圖 ====
    plt.scatter(D, I, color='red')
    plt.plot(D, lm.predict(np.reshape(D, (len(D), 1))), color='orange', linewidth=3)
    plt.plot(to_be_predicted_x, predicted_y, color = 'red', marker = 'D', markersize = 10)

    plt.xlabel("Distance", fontweight = "bold")   # 設定x座標標題及粗體
    plt.ylabel("Income", fontweight = "bold")   # 設定y座標標題及粗體
    plt.show()

else:
         print("車站距離需大於0")

