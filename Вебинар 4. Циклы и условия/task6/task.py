def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    tpl = num_tuple
    numb = '('
    for i in range(3):
        numb = (numb + str(tpl[i]))
    numb += ') '
    for i in range(3, 6):
        numb = (numb + str(tpl[i]))
    numb += '-'
    for i in range(6, 10):
        numb = (numb + str(tpl[i]))
    str_phone = numb
    return str_phone
