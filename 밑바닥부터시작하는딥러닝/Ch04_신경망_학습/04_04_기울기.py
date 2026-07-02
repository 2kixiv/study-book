### 4.4 기울기

import sys, os
sys.path.append(os.pardir)
import numpy as np

from common.gradient import numerical_gradient

def func_2(x):
    return x[0] ** 2 + x[1] ** 2 # f(x0, x1) = x0^2 + x1^2

# (3, 4), (0, 2), (3, 0) 에서의 기울기
print(numerical_gradient(func_2, np.array([3.0, 4.0]))) # [6, 8]
print(numerical_gradient(func_2, np.array([0.0, 2.0]))) # [0, 4]
print(numerical_gradient(func_2, np.array([3.0, 0.0]))) # [6, 0]



### 4.4.1 경사법 (경사 하강법)

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

# f(x0, x1) = x0^2 + x1^2 최소값 찾기
init_x = np.array([-3.0, 4.0])
print(gradient_descent(func_2, init_x=init_x, lr=0.1, step_num=100)) # (0, 0)에 근사

# 학습률이 큰 경우
init_x = np.array([-3.0, 4.0])
print(gradient_descent(func_2, init_x=init_x, lr=10.0, step_num=100)) # 발산

# 학습률이 작은 경우
init_x = np.array([-3.0, 4.0])
print(gradient_descent(func_2, init_x=init_x, lr=1e-10, step_num=100)) # (-3, 4)에서 거의 갱신되지 않음



### 4.4.2 신경망에서의 기울기

from common.loss_functions import cross_entropy_error
from common.activation_functions import softmax

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)
    
    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

net = simpleNet()
print(net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
print(np.argmax(p))

t = np.array([0, 0, 1])
print(net.loss(x, t))

f = lambda w : net.loss(x, t)
dW = numerical_gradient(f, net.W)
print(dW)