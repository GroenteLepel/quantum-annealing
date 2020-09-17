import dimod

# f(s) = 0.1 s_1 + 0.1 s_2 - 0.2 s_1 s_2
external_force = {
    0: 0.1,
    1: 0.1
}

coupler_strengths = {
    (0, 1): -0.2
}

bqm = dimod.BinaryQuadraticModel.from_ising(external_force, coupler_strengths)

# ExactSolver() is a simple exact solver for testing and debugging code using
#  your local CPU
response = dimod.ExactSolver().sample(bqm)
print(response)
