### 4.2.1 오차제곱합

import numpy as np

y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

from loss_functions import sum_squares_error

print(sum_squares_error(y, t))



### 4.2.2 교차 엔트로피 오차

from loss_functions import cross_entropy_error

print(cross_entropy_error(y, t))



### 4.2.3 미니배치 학습

import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]



### 4.2.4 (배치용) 교차 엔트로피 오차 구현하기

from loss_functions import cross_entropy_error