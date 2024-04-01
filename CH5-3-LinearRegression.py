
"""
# 機器學習 HW5-2

用學生的身高&腰圍來預測體重
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
h = np.array([160, 165, 167,170, 165, 167, 178, 182, 175, 172])
                   
westline = np.array ([67, 68, 70, 65, 80, 85, 78, 79, 95, 89]) # 身高與腰圍

w = np.array([50, 60, 65, 65 ,70, 75, 80, 85, 90, 81]) # 體重


# ==== 建立一個線性迴歸模型 ====
lm = LinearRegression()
lm.fit (np.reshape(h,  (len(h), 1)), # 將資料放進模型內訓練
           np.reshape(w, (len(w), 1)))

# ==== 預測 ====
print("依序由身高預測體重，再由腰圍預測體重")
m = float(input("輸入身高:  ")) # Element you want to input 可以輸入小數點
to_be_predicted1 = np.array([m])           
predicted_1 = lm.predict(np.reshape(to_be_predicted1, (len(to_be_predicted1), 1)))

w0 = lm.coef_         # 斜率係數
w1 = lm.intercept_ # 截距
# y =  w_1x + w_0

# ==== 繪圖 ====
plt.scatter(h, w, color='black')
plt.plot(h, lm.predict(np.reshape(h, (len(h), 1))), color='blue', linewidth=3)
plt.plot(to_be_predicted1, predicted_1, color = 'red', marker = '^', markersize = 10)

plt.xlabel("Heights (cm)", fontweight = "bold")   # 設定x座標標題及粗體
plt.ylabel("Weights (kg)", fontweight = "bold")   # 設定y座標標題及粗體
plt.show()

# ==== 建立一個線性迴歸模型 ====
lm = LinearRegression()
lm.fit (np.reshape(westline,  (len(westline), 1)), # 將資料放進模型內訓練
           np.reshape(w, (len(w), 1)))

# ==== 預測 ====
n = float(input("輸入腰圍:  ")) # Element you want to input 可以輸入小數點
to_be_predicted_x = np.array([n])           
predicted_y = lm.predict(np.reshape(to_be_predicted_x, (len(to_be_predicted_x), 1)))

w0 = lm.coef_         # 斜率係數
w1 = lm.intercept_ # 截距
# y =  w_1x + w_0

# ==== 繪圖 ====
plt.scatter(westline, w, color='red')
plt.plot(westline, lm.predict(np.reshape(westline, (len(westline), 1))), color='orange', linewidth=3)
plt.plot(to_be_predicted_x, predicted_y, color = 'red', marker = 'D', markersize = 10)

plt.xlabel("Weistline (cm)", fontweight = "bold")   # 設定x座標標題及粗體
plt.ylabel("Weights", fontweight = "bold")   # 設定y座標標題及粗體
plt.show()
