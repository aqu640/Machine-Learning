"""
#機器學習 hw9
梯度下降法 多變數函數
"""
import numpy as np
import matplotlib.pyplot as plt

def L(w):
    return w* w #  L(w) = w2
    
def dL(w):      # df: 目標函數的一階導函數
    return 2*w  # 𝝏L(w)/𝝏w= 2w
    
def gradient(w_start, df, lr, epoch): # Gradient 梯度
    w_gd = []
    w_gd.append(w_start)
    pre_w = w_start
    for cycle in range(epoch):   # w1 = w0 – α *𝝏L(w)/𝝏w𝟎
        w = pre_w - lr*df(pre_w) # 要改變的幅度
        w_gd.append(w)
        pre_w = w
    return np.array(w_gd) # 在每次反覆運算後的位置
def gradient(w_start, df, lr, epoch): # Gradient 梯度
    w_gd1 = []
    w_gd1.append(w_start)
    pre_w = w_start
    for cycle in range(epoch):   # w1 = w0 – α *𝝏L(w)/𝝏w𝟎
        w = pre_w - lr*df(pre_w) # 要改變的幅度
        w_gd1.append(w)
        pre_w = w
    return np.array(w_gd1) # 在每次反覆運算後的位置


w0 = 2    # 起始權重是2
epoch = 5 # 執行運算週期數
lr = 0.1  # learning rate 學習率0.1
# 梯度下降法 
w_gd = gradient(w0, dL, lr, epoch)
w1 = 4
w_gd1 = gradient(w1, dL, lr, epoch)


print("w_gd=",w_gd)
print("w_gd1=",w_gd1)

t = np.arange(-5.5, 5.5 , 0.01)
plt.plot(t, L(t), c= 'b')
plt.plot(w_gd, L(w_gd), c= 'r', label =  'lr={}'.format(lr))
plt.scatter(w_gd, L(w_gd),c= 'r')
plt.legend()
plt.show






    
    
    