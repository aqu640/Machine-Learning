"""
# 機器學習作業8-1
利用Matplotlib套件畫出這三個函數
	Sigmoid函數
	ReLU函數
	Tanh雙曲函數
https://www.guyuehome.com/42052
"""
# ==== Numpy套件 ====
import numpy as np
import matplotlib.pyplot as plt

# ==== 啟動函數 Sigmoid的公式 ====
def plot_sigmoid():
    x = np.arange(-6, 6, 0.15) # x = (起點，终點，間距)
    y = 1/(1+ np.exp(-x))            # 將x映射到 [0, 1] 之間
    plt.title("numpy.sigmoid()") 
    plt.plot(x, y, color = 'red', marker = "o")
    plt.show() 

# ==== 啟動函數 relu函數的公式 ====
# ReLU在x大於0梯度不變，x小於0，輸出0  
def plot_ReLU():
    X = np.arange(-5.0, 5.0, 0.08)
    Y = np.maximum(0, X)
    plt.plot(X, Y, color = 'orange', marker = "o")
    plt.ylim(-1.0, 5.5) # y軸範圍
    plt.title("numpy.relu()")
    plt.show()

# ==== 啟動函數 tanh函數的公式 ====
def tanh():
    x1 = np.linspace(-6, 6, 88) 
    y1 = np.tanh(x1) # 輸出範圍是在-1~1之間
    plt.plot(x1, y1, color = 'yellow', marker = "o") 
    plt.title("numpy.tanh()") 
    plt.xlabel("X") 
    plt.ylabel("Y") 
    plt.show()   

if __name__ == '__main__':
    plot_sigmoid()
    plot_ReLU()
    tanh()
    
    