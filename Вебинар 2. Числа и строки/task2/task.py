def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # todo Здесь нужно написать код
    discriminant = (b**2) - (c * 4)
    x1 = round(((-1) * (b) + (discriminant**0.5)) / 2, 2)
    x2 = round(((-1) * (b) - (discriminant**0.5)) / 2, 2)
    return x1, x2
