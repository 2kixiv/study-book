import numpy as np

def sum_squares_error(y, t):
    return 0.5 * np.sum((y - t)**2)

def cross_entropy_error(y, t, one_hot_label=True):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    delta = 1e-7 # log에 0이 입력이 되는 경우 INF 방지

    if one_hot_label:
        return -np.sum(t * np.log(y + delta)) / batch_size
    else:
        return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size