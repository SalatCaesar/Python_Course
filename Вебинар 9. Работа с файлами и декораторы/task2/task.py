def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    with open(file_path, 'r', encoding='utf-8') as file:
        file = [i.strip() for i in file.readlines()]
        file = ','.join(file)
        file = file.split(',,')
        most_expensive_purchases = []
        for i in file:
            i = [int(n) for n in i.split(',')]
            purch = sum(i)
            most_expensive_purchases.append(purch)
        most_expensive_purchases = sum(sorted(most_expensive_purchases)[-3:])
    return most_expensive_purchases