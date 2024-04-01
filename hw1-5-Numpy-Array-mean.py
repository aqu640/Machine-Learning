"""
# 機器學習 HW1-5
# 印出每位學生的平均分數 (五個科目 五個學生)
"""
import numpy as np                    # 將numpy縮寫

list2 = [80, 75, 88, 80, 78,
         88, 86, 90, 95, 86,
         92, 85, 92, 98, 90,
         81, 88, 80, 82, 85,
         75, 80, 78, 80, 70]          # 設定list

M1 = np.array(list2).reshape(5, 5)    # 改變維度設定為5X5矩陣

student1 = np.mean(M1[0, :])          # 取第0列全部的平均
student2 = np.mean(M1[1, :])
student3 = np.mean(M1[2, :])
student4 = np.mean(M1[3, :])
student5 = np.mean(M1[4, :])          

print("以下為學生的平均成績",'\n'       # print印出答案，str把數字轉成文字，'\n'換行
      "學生1:" , str(student1), '\n',  
      "學生2:" , str(student2), '\n',
      "學生3:" , str(student3), '\n',
      "學生4:" , str(student4), '\n',
      "學生5:" , str(student5), '\n')

