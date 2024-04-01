"""
# 機器學習 HW2-1
請繪製三條曲線
# y1 = x**1
# y2 = x**2
# y3 = x**3
繪製紅色虛線、藍色正方形，綠色上三角形
x的起始值是0、終止值為5、間隔值為0.1的數列
"""
import matplotlib.pyplot as plt # 定義matplotlib.pyplot並將其縮寫
import numpy as np              # 定義numpy並將其縮寫

x = np.arange (0, 5, 0.1)  # (起始值、終止值、間隔值) = (0,5,0.1)
y = np.square (x)
plt.plot (x, x, "r--",     # "--"虛線 "r" 紅色
          x, x ** 2 ,"bs", # "b" 藍色 "s" 正方形
          x, x ** 3, "g^") # "g" 綠色 "^" 三角
plt.show ()

# plt.plot (x, y)
# 用x**2 非 x^2
# 用show 非 print
# 點選右上角 plot 看結果



