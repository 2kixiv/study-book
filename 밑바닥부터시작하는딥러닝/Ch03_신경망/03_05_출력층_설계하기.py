### 3.5.1 항등 함수와 소프트맥스 함수 구현하기

import numpy as np

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)
sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
y = exp_a / sum_exp_a
print(y)



### 3.5.2 소프트맥스 함수 구현 시 주의점

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a))) # [nan nan nan] 오버플로우

c = np.max(a)
print(np.exp(a - c) / np.sum(np.exp(a - c)))



### 3.5.3 소프트맥스 함수의 특징

from activation_functions import softmax

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y) # [0.01821127 0.24519181 0.73659691] 확률로 해석 가능
print(np.sum(y)) # 1.0