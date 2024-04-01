"""
# 機器學習 HW2-3
# 根據統計資料繪製長條圖
"""

import matplotlib.pyplot as plt # 定義matplotlib.pyplot並將其縮寫

x = [70, 80, 90, 100, 110, 120, 130, 140, 150]         # x (x軸)
y = [2.2, 5.3, 11.5, 19.7, 22.9, 19.6, 11.2, 5.5, 2.1] #(y軸)

tl = ["<75","75~84","85~94", "95~104","105~114","115~124","125~134","135~144",">144"]
                                                       # tick_label 座標軸文字
color = ['navy','blueviolet','crimson','r','darkorange','yellow','lime','deepskyblue']
                                                       # 可查顏色表

plt.legend(loc = "best")          # 設定圖例及其位置為最佳
plt.figure(figsize = (8.4, 4.2))  # 可用小數點，更改圖片比例
plt.bar(x,color = color,
        height = y,               # height 長條圖高度
        width = 5,                # width	寬度
        tick_label = tl,          # tick_label 座標軸文字
        label = "<75,>144")

"""
# bar() 改為 barh()，就會變成水平的長條圖 
# 如果改成水平長條圖，參數 width 要改成 height )
"""
plt.legend()
plt.xlabel("Intelligenzquotient") # 智商IQ
plt.ylabel("Probability (%)")     # 人數百分比
plt.title("Bar of IQ")            # 智商(IQ)長條圖
plt.show()

# 座標標題只能用英文，中文不會顯示
# 也可用載入txt
"""
智商(IQ)分組	人數百分比(%)
低於75　　	2.2
75~84　　	5.3
85~94　　	11.5
95~104　　	19.7
105~114	　　22.9
115~124	　　19.6
125~134	　　11.2
135~144	　　5.5
高於144	　　2.1
"""
