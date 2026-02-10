def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    qwer = {}
    dct = str()
    for q, w, e, r in cats_data:
        qwer.setdefault((e, r), [])
        qwer[(e, r)].append(f"{q}, {w}")
    for a, b in (qwer.items()):
        dct += (' '.join(a) + ': ' + '; '.join(b) + '\n')
    return dct
