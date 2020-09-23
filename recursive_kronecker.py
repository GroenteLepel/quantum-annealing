import numpy as np


def pauli_z():
    return np.array([[1, 0], [0, -1]])


def identity():
    return np.eye(2)


def rec_krons(max_n: int, i: int, j: int = None):
    """Calculate the chain of kronecker products of length max_n with a
    pauli_z matrix at the ith location.

    Note:
        adding the j value makes this a quadratic term by adding a pauli_z
        matrix at the jth location as well.
    """
    if max_n == 1:
        # reach the end of the loop
        if i == 1 or j == 1:
            # return pauli_z if this is the spot for the pauli_z
            return pauli_z()
        else:
            # else return the identity matrix
            return identity()
    elif max_n == i or max_n == j:
        # reached the part where the pauli z needs to be added
        return np.kron(rec_krons(max_n - 1, i, j), pauli_z())
    else:
        return np.kron(rec_krons(max_n - 1, i, j), identity())

