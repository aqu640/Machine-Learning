"""
# 機器學習 HW5-2

用學生的身高來預測體重
pip install scikit-learn
"""
# ==== 導入 pandas numpy & 線性迴歸模組 模組 ====

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression


# ==== 建立身高與體重的 Numpy 陣列 ====
h = np.array([147.9, 163.5, 159.8, 155.1, 163.3, 158.7, 172.0, 161.2, 153.9, 161.6]) # 身高
w = np.array([41.7, 60.2,47.0, 53.2, 48.3, 55.2, 58.5, 49.0, 46.7, 52.5])                      # 體重

# ==== 建立一個模型 model 為線性迴歸模型 ====
lm = LinearRegression()
# ==== 將資料放進模型內訓練 ====
lm.fit (np.reshape(h,  (len(h), 1)),
           np.reshape(w, (len(w), 1)))

# ==== 預測 ====
m = float(input("輸入男學生的身高:  ")) # Element you want to input 可以輸入小數點
to_be_predicted1 = np.array([m])           
predicted_1 = lm.predict(np.reshape(to_be_predicted1, (len(to_be_predicted1), 1)))



w0 = lm.coef_         # 斜率係數
w1 = lm.intercept_ # 截距
# y =  w_1x + w_0

# ==== 繪圖 ====
plt.scatter(h, w, color='black')
plt.plot(h, lm.predict(np.reshape(h, (len(h), 1))), color='blue', linewidth=3)
plt.plot(to_be_predicted1, predicted_1, color = 'red', marker = '^', markersize = 10)

plt.xticks(())
plt.yticks(())
plt.show()
