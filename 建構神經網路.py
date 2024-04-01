"""
# 機器學習 HW7
# 建構神經網路
# 感知器實現AND邏輯閘:
# 有2個輸入x1與x2，和一個輸出out，其符號和真值表
# 初始權重w1和w2得初值為1，
# 偏權值b為-0.5，輸出f(n)的門檻值為0
"""
# ==== 導入模組 ====
import numpy as np

# ==== 設定感知器 y = w1*x1 + w2*x2 + b ====
def AND1(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1])     # W 為權重 weight
    b = -0.5                 # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0             # 小於等於1 就輸出0
    else:
        return 1             # 大於1 就輸出1
    
# ==== 修正網路 b=0 ====
def AND2(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1])     # W 為權重 weight
    b = 0                    # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0             # 小於等於1 就輸出0
    else:
        return 1             # 大於1 就輸出1
    
# ==== 修正網路 b=-1 ====
def AND3(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1])     # W 為權重 weight
    b = -1                   # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0             # 小於等於1 就輸出0
    else:
        return 1             # 大於1 就輸出1

# ==== 建構神經網路 ====
if __name__ == '__main__': # 程式執行

    # 第一列輸入值：x1=0 和 x2=0
    for val in [(0, 0)]:   
        # 和真值表的輸出0相同，不用調整權重W 和偏向量b
        print("當(x1,x2)=",str(val) + " -> " + str(AND1(val[0], val[1])),"輸出正確\n")
        
    # 二列輸入值：x1=0 和 x2=1:     
    for val in [(0, 1)]:   
        # 真值表的輸出0不同，需要調整權重W 或偏向量b
        print("當(x1,x2)=",str(val) + " -> " + str(AND1(val[0], val[1])),"\n輸出錯誤，第1次修正網路\n")
        
        # 增加偏向量b值，將b值增加0.5成為0，重新計算
        print("b = 0時\n當(x1,x2)=",str(val) + " -> " + str(AND2(val[0], val[1])),"\n輸出錯誤，第2次修正網路\n")
        
        # 減少偏向量b值，將b值減-1成為-1，重新計算，輸出正確
        print("b = -1時\n當(x1,x2)=",str(val) + " -> " + str(AND3(val[0], val[1])),"輸出正確\n")
        
    # 第三列輸入值：x1=1 和 x2=0:   
    for val in [(1, 0)]:   
        # 和真值表的輸出0相同
        print("當(x1,x2)=",str(val) + " -> " + str(AND3(val[0], val[1])),"輸出正確\n")
        
    # 第四列輸入值：x1=1 和 x2=1:   
    for val in [(1, 1)]:
        # 和真值表的輸出0相同       
        print("當(x1,x2)=",str(val) + " -> " + str(AND3(val[0], val[1])),"輸出正確")
