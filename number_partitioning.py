import numpy as np
import dimod


def ising_model():
    # f(s) = 0.1 s_1 + 0.1 s_2 - 0.2 s_1 s_2
    external_force = {
        1: 0.1,
        4: 0.1,
        5: 0.1
    }

    coupler_strengths = {
        (1, 4): -0.2,
        (1, 5): -0.2,
        (4, 5): -0.2,
    }

    # bqm = dimod.BinaryQuadraticModel.from_ising(external_force,
    #  coupler_strengths)
    bqm = dimod.BinaryQuadraticModel(external_force, coupler_strengths, 0.0,
                                     dimod.BINARY)

    # ExactSolver() is a simple exact solver for testing and debugging code
    #  using your local CPU. calculates eigenvectors and eigenvalues on CPU
    response = dimod.ExactSolver().sample(bqm)
    return response


def qubo_model():
    numbers = np.array([1, 4, 5])
    total = np.sum(numbers)
    qubo_array = np.zeros((len(numbers), len(numbers)))

    linear = numbers * (numbers - total)
    quadratic = np.outer(numbers, numbers)

    qubo_array = quadratic
    np.fill_diagonal(qubo_array, linear)

    model = dimod \
        .BinaryQuadraticModel \
        .from_numpy_matrix(
            qubo_array,
            [1, 4, 5]
        )

    response = dimod.ExactSolver().sample(model)
    return response


if __name__ == '__main__':
    print(qubo_model())
