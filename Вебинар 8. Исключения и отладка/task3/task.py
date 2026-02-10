def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """
    # todo Здесь нужно написать код
    try:
        s = first_point[0] + first_point[1] + second_point[0] + second_point[1]
        return s
    except Exception as e:
        return str(e)[::-1]



