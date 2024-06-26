"""
# 機器學習 HW5-3
# K-means演算法
在K=3的情況下
使用K-means演算法替14隻動物進行分群。

pip install scikit-learn
"""
# ====  導入繪圖套件  ====
import matplotlib.pyplot as plt

# ====   Python 數據處理套件  ====
import numpy as np

# ====  導入迴歸模型套件  ====
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans


# ==== 建立 Numpy 陣列 ====
data = np.array([[ 51, 10.2], [ 46, 8.8 ],[ 51, 8.1 ],
                          [ 45, 7.7 ],[51, 9.8 ],[ 50, 7.2  ],
                          [ 33, 4.8 ], [ 38, 4.6  ], [ 37, 3.5 ],
                          [ 33, 3.3], [ 33, 4.3], [ 21, 2.0  ] ,
                          [ 23, 1.0 ], [ 24, 2.0]])    # 身長與體重    

# ====   用 KMeans 在資料中找出 3個分組 ====
ks = KMeans(init="k-means++",n_clusters=3 ).fit(data) # 挑出 3 個中心數據
labels =  ks.labels_
cluster = ks.cluster_centers_
plt.scatter( data[ : , 0 ], data[ : , 1 ] )        # ( x, y )
plt.scatter( cluster[ : , 0 ], cluster[ : , 1 ] ) # ( x, y )

print("the labels is\n",labels,"\n")
print("the cluster centers is\n",cluster)

plt.show()
    


