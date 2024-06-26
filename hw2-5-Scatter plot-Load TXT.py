"""
# 機器學習 HW2-5
# 從HW.txt檔案載入身高與體重資料
# 請根據該檔案的資料繪製散佈圖
# X軸為身高、Y軸為體重。
"""
import matplotlib.pyplot as plt # 定義matplotlib.pyplot並將其縮寫
import numpy as np              # 定義numpy並將其縮寫

# "HW.txt"有絕對路徑與相對路徑
# 相對路徑要放在同一個資料夾才能讀取

HW = np.loadtxt("HW.txt", delimiter = ",")  # delimiter 分隔符號，預設逗號
Heights = HW[:, 0]              # 取第0行的全部
Weights = HW[:, 1]
plt.scatter(Heights,            # scatter 散布圖
            Weights,
            c = "navy",         # 點顏色
            s = 2000,           # 點大小
            alpha = .8,         # 透明度，預設 1，範圍0~1( 完全透明 ~完全不透明 )
            marker = "$ˁ˙˟˙ˀ$", # 點以框框內符號表示
            linewidths = 1)     # 資料點外框粗細，預設無外框    

plt.xlabel("Heights (cm)", fontweight = "bold")   # 設定x座標標題及粗體
plt.ylabel("Weights (kg)", fontweight = "bold")   # 設定y座標標題及粗體
plt.title("Scatter of Heights and Weights",
          fontsize = 15,
          fontweight = "bold")  # 設定標題、字大小及粗體
plt.legend(loc = "best")        # 設定圖例及其位置為最佳
plt.show()

# cmap='Set1'   使用 Set1 的 colormap
# vmin=,vmax=   對照顏色地圖的最大 最小值
# linewidths	資料點外框粗細，預設無外框，支援陣列資料
# edgecolors	資料點外框顏色，預設無外框，顏色設定等同 c   
