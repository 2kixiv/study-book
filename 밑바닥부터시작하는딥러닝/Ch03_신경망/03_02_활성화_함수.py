### 3.2.2 계단 함수 구현하기

from activation_functions import step_function

import numpy as np

print(step_function(np.array([-1.0, 1.0, 2.0])))



### 3.2.3 계단 함수의 그래프

import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()



### 3.2.4 시그모이드 함수 구현하기

from activation_functions import sigmoid

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()



### 3.2.7 ReLU 함수

from activation_functions import relu
