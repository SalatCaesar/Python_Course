def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    p = lst.count(0)
    for i in range(p):
        lst.remove(0)
    for i in range(p):
        lst.append(0)
    return lst
