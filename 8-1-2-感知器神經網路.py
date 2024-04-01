"""
# 機器學習8-2
完成以下多感知器神經網路的正向傳播
輸入與輸出資料
(0, 0) -> 0
(0, 1) -> 1
(1, 0) -> 1
(1, 1) -> 0
"""
# ==== 設定感知器 ====
import numpy as np
def AND1(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1])     # W 為權重 weight
    b = -0.5                 # 偏權值 bias
    tmp = np.sum(W*x) + b 
    
    if x1==1 and x2 ==1 :
        return 0
    elif tmp <= 0:
        return 0 # 小於等於1 就輸出0
    else:
        return 1 # 大於1 就輸出1
    
if __name__ == '__main__':
    for val in [(0, 0)]: # 真值表
        y1 = AND1(val[0], val[1])
        print("\n當(x1,x2)=",str(val) + " -> " + str(y1))
        
    for val in [(0, 1)]: # 真值表 
        y2 = AND1(val[0], val[1])
        print("\n當(x1,x2)=",str(val) + " -> " + str(y2))
    
    for val in [(1, 0)]: # 真值表 
        y5 = AND1(val[0], val[1])
        print("\n當(x1,x2)=",str(val) + " -> " + str(y5))

    for val in [(1, 1)]: # 真值表         
        y6 = AND1(val[0], val[1])
        print("\n當(x1,x2)=",str(val) + " -> " + str(y6))
