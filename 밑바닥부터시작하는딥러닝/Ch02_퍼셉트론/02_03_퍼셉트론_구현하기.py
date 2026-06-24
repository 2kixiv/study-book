### 2.3.1 간단한 구현부터

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x1 + w2 * x2
    return int(tmp >= theta)

AND(0, 0) # 0
AND(1, 0) # 0
AND(0, 1) # 0
AND(1, 1) # 1



### 2.3.2 가중치와 편향 도입

import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(np.sum(w * x) + b)



### 2.3.3 가중치와 편향 구하기
# gates.py에 구현