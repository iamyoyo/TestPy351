import numpy as np  # use the np instead of nympy
a = np.array([2, 0, 1, 6])  # 创建数组，需要空白
print(a)
print(a[:3])
print(a.min())  # 如果没有新行,最后一样要加两个空格
a.sort()
print(a)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b*b)
