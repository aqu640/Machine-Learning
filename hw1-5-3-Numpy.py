"""
# 機器學習 HW1-5(3)
# 印出每位學生成績的中位數、標準差與變異數
"""
import numpy as np                    #將numpy縮寫

list2 = [80, 75, 88, 80, 78,
         88, 86, 90, 95, 86,
         92, 85, 92, 98, 90,
         81, 88, 80, 82, 85,
         75, 80, 78, 80, 70]          #設定list

M1 = np.array(list2).reshape(5, 5)    #設定為5X5矩陣

student1_m = np.median(M1[0, :])      #取第0列全部的中位數
student2_m = np.median(M1[1, :])
student3_m = np.median(M1[2, :])
student4_m = np.median(M1[3, :])
student5_m = np.median(M1[4, :])   

student1_s = np.std(M1[0, :])         #取第0列全部的標準差
student2_s = np.std(M1[1, :])
student3_s = np.std(M1[2, :])
student4_s = np.std(M1[3, :])
student5_s = np.std(M1[4, :]) 

student1_v = np.var(M1[0, :])         #取第0列全部的變異數
student2_v = np.var(M1[1, :])
student3_v = np.var(M1[2, :])
student4_v = np.var(M1[3, :])
student5_v = np.var(M1[4, :])        

print("以下是學生成績的中位數(median)、標準差(sd)、變異數(var)",'\n',
      "學生1 median:" , str(student1_m),'\n' ,
      "sd:", str(student1_s),'\n' ,
      "var:", str(student1_v ),'\n' ,'\n',
      "學生2 median:" , str(student2_m),'\n' ,
      "sd:", str(student2_s),'\n' ,
      "var:", str(student2_v ), '\n','\n',
      "學生3 median:" , str(student3_m),'\n' ,
      "sd:", str(student3_s),'\n' ,
      "var:", str(student3_v ),'\n','\n',
      "學生4 median:" , str(student4_m),'\n' ,
      "sd:", str(student4_s),'\n' ,
      "var:", str(student4_v ),'\n','\n',
      "學生5 median:" , str(student5_m),'\n' ,
      "sd:", str(student5_s),'\n' ,
      "var:", str(student5_v )
      )
"""
median()
中位數

stdev()
數據的樣本標準差

variance()
數據的樣本變異數
"""

# print印出答案，str把數字轉成文字
# ,'\n' ,換行