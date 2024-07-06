import numpy as np
a = np.array([5,7,3,1,4,3])
print(a)

#リストの2次元配列
b = a.reshape([3,2])
print(b)

#全てのパラメータを0で初期化
c = np.zeros((3,4))
print(c)

#配列の各要素をランダム化
np.random.seed(0)
r = np.random.rand(3,4)
print(r)