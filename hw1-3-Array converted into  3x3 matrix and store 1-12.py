"""
# 機器學習 HW1-3
# 產生一維串列，內容存放1-12的元素
# 並轉換成3x4矩陣。
"""
import numpy as np   #將numpy縮寫

list3 = [1, 2, 3,
         4, 5, 6,
         7, 8, 9,
         10, 11, 12]               # 設定串列
print ("串列","\n", list3)         # print印出答案
A = np.array(list3).reshape(3, 4)  # 改變陣列的維度
print("3x4矩陣","\n",A)            # print印出答案
