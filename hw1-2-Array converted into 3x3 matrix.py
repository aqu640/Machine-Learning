"""
# 機器學習 HW1-2
# 產生一串列內容存放2-10的元素
# 並轉換成3x3矩陣。
"""

import numpy as np                   # 將numpy縮寫

list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10] # 設定串列
print ("串列","\n", list2)           # print印出答案
A = np.array(list2).reshape(3, 3)    # 改變陣列的維度
print("3x3矩陣","\n",A)              # print印出答案
