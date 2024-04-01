"""
# 機器學習 HW2-2
根據下列4個函數，繪製4個圖表
x的範圍為: -10~10:
# y1 = x**1
# y2 = x**2
# y3 = x**3
# y4 = x**4
"""
import numpy as np              # 定義numpy並將其縮寫
import matplotlib.pyplot as plt # 定義matplotlib.pyplot並將其縮寫
x = np.arange(0, 5, 0.1)        # (起始值、終止值、間隔值) = (0,5,0.1)

y1 = x    # 次方用** 非^2
y2 = x**2
y3 = x**3
y4 = x**4 

P1 = plt.plot (x, y1, "mh")  # m 洋紅 # hexagon1
P2 = plt.plot (x, y2, "rP")  # r 紅   # plus
P3 = plt.plot (x, y3, "b*")  # b 藍   # star
P4 = plt.plot (x, y4, "co")  # c 青   # o 圓點

plt.axis ([0, 5, -3, 35])    # x範圍0~5, y範圍-3~35
plt.grid ()                  # grid 網格，方便對照座標
plt.show ()                  # 生成圖表

"""
# axis 軸
# o 圓點
"""

