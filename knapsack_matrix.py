import numpy as np


def knapsack_matrix(w, c, W_max, A, B):
    w = np.array(w)
    c = np.array(c)

    # Helper array [1, 2, ..., W_max]
    N = np.arange(1, W_max + 1)

    # Initialize the matrix of size W_max + m
    out = np.zeros((W_max + len(w), W_max + len(w)))

    # Adding the Ha part
    out[:W_max, :W_max] += A * -2 * np.identity(W_max)
    out[:W_max, :W_max] += A * np.ones((W_max, W_max))
    out[:W_max, :W_max] += A * N[:, np.newaxis] * N[np.newaxis, :]
    out[W_max:, W_max:] += A * w[:, np.newaxis] * w[np.newaxis, :]
    out[:W_max, W_max:] += A * -N[:, np.newaxis] * w[np.newaxis, :]
    out[W_max:, :W_max] += A * -w[:, np.newaxis] * N[np.newaxis, :]

    # Adding the Hb part
    out[W_max:, W_max:] += -B * np.diag(c)
