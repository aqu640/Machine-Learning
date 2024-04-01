"""
# 機器學習 HW1-1
# 使用NumPy計算sin0°、sin30°、sin45°、
# cos30°、cos45°、cos60°、
# tan30°、tan45°、tan60°的值。

"""
import numpy as np    # 定義numpy並將numpy縮寫

print("三角函數的值為","\n",
      "sin0° =",np.sin(np.pi*0),"\n",
      "sin30°=",np.sin(np.pi/6),"\n",
      "sin45°=",np.sin(np.pi/4),"\n","\n",
      "cos30°=",np.cos(np.pi/6),"\n",
      "cos45°=",np.cos(np.pi/4),"\n",
      "cos60°=",np.cos(np.pi/3),"\n","\n",
      "tan30°=",np.tan(np.pi/6),"\n",
      "tan45°=",np.tan(np.pi/4),"\n",
      "tan60°=",np.tan(np.pi/3))
"""
# np.pi可被讀取為符號pi
# 360度 = 2pi
# 60度 = 1/3*pi
# 列印出結果
"""
