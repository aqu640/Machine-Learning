
"""
#機器學習 hw9
梯度下降法 
多變數函數
"""
import numpy as np
import matplotlib.pyplot as plt

def L(w1,w2):
    return w1**2 + w2**2 #  L(w) = w2
    
def dL(w):      # df: 目標函數的一階導函數
    return 2*[w1,w2]  # 𝝏L(w)/𝝏w= 2w
    
def gradient(w_start, df, lr, epoch): # Gradient 梯度
    
    w_gd = []
    # w_gd.append(w_start)
    
    pre_w1 = w_start[0]
    pre_w2 = w_start[1]

    for cycle in range(epoch):   # w1 = w0 – α *𝝏L(w)/𝝏w𝟎
        if cycle != 40:
            w1 = pre_w1 - lr*df(pre_w1) # 要改變的幅度
            w2 = pre_w2 - lr*df(pre_w2) # 要改變的幅度

            pre_w1 = w1
            pre_w2 = w2
        else :
            w_gd.append(pre_w1)
            w_gd.append(pre_w2)
            print('w_gd',w_gd)
    return np.array(w_gd) # 在每次反覆運算後的位置

        

w1 = 2
w2 = 4
w0 = [w1, w2]    # w0初始是[2, 4]
print("初始 w0 = ",w0)
epoch = 1 # 執行運算週期數
lr = 0.1  # learning rate 學習率0.1
# 梯度下降法 
w_gd = gradient(w0, dL, lr, epoch)

print("w_gd=",w_gd)
t = np.arange(-5.5, 5.5 , 0.01)
plt.plot(t, L(t), c= 'b')
plt.plot(w_gd, L(w_gd), c= 'r', label =  'lr={}'.format(lr))
plt.scatter(w_gd, L(w_gd),c= 'r')
plt.legend()
plt.show






    
    
    