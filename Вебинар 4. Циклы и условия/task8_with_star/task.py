def max_division_by_3(num):
    """Преобразование числа
    :param num: натуральное число
    :return: другое натуральное число, удовлетворяющее условиям
    """
    # todo Здесь нужно написать код
    num = str(num)
    p = None
    c = 9
    i = 0
    b = int(num)
    while p != 0:
        if int(b) < int(num):
            i += 1
            c = 9
        b = str(num[:i]) + str(c) + str(num[i + 1:])
        c -= 1
        if b == str(num):
            continue
        if c == 0:
            i += 1
            c = 9
        p = 0
        p += int(b)
        p = p % 3
    new_num = int(b)
    return new_num
