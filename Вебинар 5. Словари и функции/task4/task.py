def scrabble(word):
    """Игра 'Эрудит'
    :param word: слово
    :return: количество очков за слово
    """
    # todo Здесь нужно написать код
    o1 = dict.fromkeys(['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
    o2 = dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2)
    o3 = dict.fromkeys(['б', 'г', 'ь', 'я'], 3)
    o4 = dict.fromkeys(['й', 'ы'], 4)
    o5 = dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5)
    o8 = dict.fromkeys(['ф', 'ш', 'э', 'ю'], 8)
    o10 = dict.fromkeys(['щ'], 10)
    o15 = dict.fromkeys(['ъ'], 15)
    o_all = {**o1, **o2, **o3, **o4, **o5, **o8, **o10, **o15}
    points = 0
    for i in range(len(word)):
        points += int(o_all[word[i]])
    return points

