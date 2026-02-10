def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    new_str = str()
    for i in range(len(our_str)):
        new_str += our_str[i] + '_' + str(our_str[0:i + 1].count(our_str[i]))
    return new_str

