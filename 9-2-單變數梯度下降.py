# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:56:04 2023

@author: r
"""

import numpy as np
import matplotlib.pyplot as plt

def L(w):
    # 定義目標函數
    x, y = w
    return x**2 + y**2

def dL(w):
    # 計算目標函數的梯度
    x, y = w
    return np.array([2*x, 2*y])

def gradient_descent(w_start, df, lr, epochs):
    w_gd = [w_start]  # 存放所有歷史權重
    pre_w = w_start
    
    for i in range(epochs):
        # 更新權重
        w = pre_w - lr * df(pre_w)
        
        # 存儲權重
        w_gd.append(w)
        
        # 更新pre_w
        pre_w = w
        
    return np.array(w_gd)

w0 = np.array([2, 4])  # 初始化權重
epochs = 40  # 迭代次數
lr = 0.1  # 學習率
w_gd = gradient_descent(w0, dL, lr, epochs)

print(w_gd)
plt.figure(figsize=(8, 6))
t1, t2 = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
t = np.c_[t1.ravel(), t2.ravel()]
z = L(t.T).reshape(t1.shape)
plt.contour(t1, t2, z, levels=np.logspace(-2, 3, 20), cmap=plt.cm.jet)
plt.plot(w_gd[:, 0], w_gd[:, 1], 'r-o')
plt.title('lr={}'.format(lr))
plt.show()
