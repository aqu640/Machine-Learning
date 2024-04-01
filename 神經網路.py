# """
# and nor都有
# https://programming727.pixnet.net/blog/post/21422747
# 可複製網址
# https://tobygao.github.io/Learning-Lounge/2018/07/21/deep-learning-1.html
# Deep Learning 深度學習
# 感知器(perceptron)，二元的線性分類器
# y =w1* x1+ w2* x2+ b

# """
# ==== 設定感知器 y = w1*x1 + w2*x2 + b ====
import numpy as np
def AND1(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1])     # W 為權重 weight
    b = -0.5                 # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0 # 小於等於1 就輸出0
    else:
        return 1 # 大於1 就輸出1
    
# ==== 修正網路 b=0 ====
def AND2(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1]) # W 為權重 weight
    b = 0                # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0 # 小於等於1 就輸出0
    else:
        return 1 # 大於1 就輸出1
    
# ==== 修正網路 b=-1 ====
def AND3(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([1, 1]) # W 為權重 weight
    b = -1                # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0 # 小於等於1 就輸出0
    else:
        return 1 # 大於1 就輸出1


if __name__ == '__main__':
    for val in [(0, 0)]: # 真值表
        y1 = AND1(val[0], val[1])
        print("當(x1,x2)=",str(val) + " -> " + str(y1))
        print("輸出正確\n")
        
    for val in [(0, 1)]: # 真值表 
        y2 = AND1(val[0], val[1])
        print("當(x1,x2)=",str(val) + " -> " + str(y2))
        print("輸出錯誤，第1次修正網路\n")
    
        y3 = AND2(val[0], val[1])
        print("當b = 0")
        print("當(x1,x2)=",str(val) + " -> " + str(y3))
        print("輸出錯誤，第2次修正網路\n")

        y4 = AND3(val[0], val[1])
        print("當b = -1")
        print("當(x1,x2)=",str(val) + " -> " + str(y4))
        print("輸出正確\n")
    
    for val in [(1, 0)]: # 真值表 
        y5 = AND3(val[0], val[1])
        print("當b = -1")
        print("當(x1,x2)=",str(val) + " -> " + str(y5))
        print("輸出正確\n")
    for val in [(1, 1)]: # 真值表         
        y6 = AND3(val[0], val[1])
        print("當(x1,x2)=",str(val) + " -> " + str(y6))
        print("輸出正確\n")

    
    
    

        


"""       
# ==== 設定感知器 y = w1*x1 + w2*x2 + b ====
def AND(x1, x2):
    x = np.array([x1, x2])   # x1、x2是輸入
    W = np.array([0.5, 0.5]) # W 為權重 weight
    b = -0.5                 # 偏權值 bias
    tmp = np.sum(W*x) + b 
    if tmp <= 0:
        return 0 # 小於等於1 就輸出0
    else:
        return 1 # 大於1 就輸出1

if __name__ == '__main__':
    for val in [(0, 0), (1, 0), (0, 1), (1, 1)]: # 真值表
        y = AND(val[0], val[1])
        print("當b=-0.5\n")
        print(str(val) + " -> " + str(y))
"""