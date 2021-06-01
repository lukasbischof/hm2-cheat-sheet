from functools import reduce


def lagrange_int(points, x_int):
    x_values = list(map(lambda e: e[0], points))
    l = lambda i: lagrange_impl(x_values, x_int, i)

    return sum([l(i) * points[i][1] for i in range(len(x_values))])


def lagrange_impl(x_values, x, i):
    """
    Implementation der l_i(x) Lagrangepolynome
    """
    ret = []
    for j in range(0, len(x_values)):
        if i != j:
            ret.append((x - x_values[j]) / (x_values[i] - x_values[j]))

    return reduce(lambda a, b: a * b, ret)


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    known_points = [(0, 1013), (2500, 747), (5000, 540), (10000, 226)]
    interpolated_value = lagrange_int(known_points, 3750)
    print(interpolated_value)
