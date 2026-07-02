### 4.3.1 미분

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)



### 4.3.2 수치 미분의 예

import numpy as np
import matplotlib.pylab as plt

def func_1(x):
    return 0.01 * x ** 2 + 0.1 * x # y = 0.01x^2 + 0.1x

x = np.arange(0.0, 20.0, 0.1)
y = func_1(x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, y)
plt.show()

# 실제 5와 10에서의 기울기 : 0.2, 0.3
print(numerical_diff(func_1, 5)) # 0.1999999999990898
print(numerical_diff(func_1, 10)) # 0.2999999999986347



### 4.3.3 편미분

def func_2(x):
    return x[0] ** 2 + x[1] ** 2 # f(x0, x1) = x0^2 + x1^2

def func_tmp1(x0):
    return x0 * x0 + 4.0 ** 2.0

def func_tmp2(x1):
    return 3.0 ** 2.0 + x1 * x1

# x0 = 3, x1 = 4 일때 편미분
print(numerical_diff(func_tmp1, 3.0)) # 6.00000000000378
print(numerical_diff(func_tmp2, 4.0)) # 7.999999999999119