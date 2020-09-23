import dimod

w = [5, 5, 1]
c = [2, 5, 10]

wmax = 8

# H = HA + HB

lin_dict = dict()
quad_dict = dict()
off_list = list()

A = 10
B = 1


def H(lin, quad, off, max_weight):
    HA(lin, quad, off, max_weight)
    HB(lin)


def HA(lin, quad, off, max_weight):
    _first_term_HA(lin, quad, off, max_weight)
    _second_term_HA(lin, quad, max_weight)


def HB(lin):
    for i in range(0, len(c)):
        index1 = 'x' + str(i + 1)
        lin[index1] += -B * c[i]


def _first_term_HA(lin, quad, off, max_weight):
    for i in range(1, max_weight + 1):
        for j in range(i, max_weight + 1):
            if i == j:
                index1 = 'y' + str(i)
                lin[index1] = -1 * A
            else:
                index1 = 'y' + str(i)
                index2 = 'y' + str(j)
                quad[(index1, index2)] = 2 * A

    off.append(A)


def _second_term_HA(lin, quad,max_weight):
    vec = list()
    for y in range(1, max_weight + 1):
        vec.append(y)
    for x in range(1, len(w) + 1):
        vec.append(-w[x - 1])
    for i in range(1, len(vec) + 1):
        for j in range(i, len(vec) + 1):
            if i == j:
                if i <= max_weight:
                    index1 = 'y' + str(i)
                    lin[index1] += A * vec[i - 1] ** 2
                else:
                    index1 = 'x' + str(i - max_weight)
                    lin[index1] = A * vec[i - 1] ** 2
            else:
                if i <= max_weight and j <= max_weight:
                    index1 = 'y' + str(i)
                    index2 = 'y' + str(j)
                    quad[(index1, index2)] += A * 2 * vec[i - 1] * vec[j - 1]
                else:
                    if i <= max_weight < j:
                        index1 = 'y' + str(i)
                        index2 = 'x' + str(j - max_weight)
                        quad[(index1, index2)] = A * 2 * vec[i - 1] * vec[j - 1]
                    else:
                        index1 = 'x' + str(i - max_weight)
                        index2 = 'x' + str(j - max_weight)
                        quad[(index1, index2)] = A * 2 * vec[i - 1] * vec[j - 1]


H(lin_dict, quad_dict, off_list, wmax)

print("\nLinear Terms \n", lin_dict)
print("\nQuadratic \n", quad_dict)
print("\nOffset Terms\n", sum(off_list))

bqm = dimod.BinaryQuadraticModel(
    lin_dict,
    quad_dict,
    sum(off_list),
    dimod.BINARY
)

sampleset = dimod.ExactSolver().sample(bqm)

print(sampleset.lowest())
