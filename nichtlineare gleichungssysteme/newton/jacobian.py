import sympy as sp

if __name__ == '__main__':
    x1, x2, x3 = sp.symbols(['x1', 'x2', 'x3'])
    x = sp.Matrix([x1, x2, x3])
    f = sp.Matrix([
        (x1 + x2 ** 2 - x3 ** 2 - 13),
        (sp.ln(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1),
        ((x2 - 3) ** 2 - x3 ** 3 + 7)
    ])

    Df = f.jacobian(x)
    print(f'Df = {Df}')

    x0 = sp.Matrix([1.5, 3, 2.5])
    g = f + Df.subs(list(zip(x, x0))) * (x - x0)
    print(f'g(x) = {g}')
