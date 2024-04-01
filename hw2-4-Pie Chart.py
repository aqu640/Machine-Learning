"""
# 機器學習 HW2-3
假設小明每天工作、睡覺、上網 & 其它活動的時間
分別為8、7、2、7小時
繪製圓形圖
# 裡面會自動算出每個活動所佔的時間比例。

"""
import matplotlib.pyplot as plt # 定義matplotlib.pyplot並將其縮寫

activities = ["job", "sleep", "Internet", "others"]    # 工作、睡覺、上網 & 其它
hours = [8, 7, 2, 7]
colors = ["coral","darkseagreen", "cadetblue", "gold"] # 顏色，可查色號表

plt.pie(hours,
        labels = activities,           # 標籤
        colors = colors,
        shadow = True,                 # 設定陰影
        textprops = {"fontsize" : 18}, # 文字大小
        explode = (0, 0, 0, 0.1),      # 設定分隔的區塊位置
        autopct = "%1.1f%%")           # 將數值百分比並留到小數點一位

plt.legend(loc = "best")               # 設定圖例及其位置為最佳
#plt.figure(figsize = (5, 5))          # 可自訂圖片比例
plt.axis("equal")                      # 使圓餅圖的比例相等
plt.title("Pie chart of daily schedule", 
          {"fontsize" : 24})           # 設定標題及其文字大小
plt.show()
