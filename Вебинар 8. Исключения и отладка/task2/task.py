class Trigon:
    def __init__(self, *cathetus):
        if len(cathetus) != 3:
            raise IndexError(f'Передано {len(cathetus)} аргументов, а ожидается 3')
        for i in cathetus:
            if not isinstance(i, int):
                raise TypeError ('Стороны должны быть числами')
        for i in cathetus:
            if i == 0 or i <= 0:
                raise ValueError ('Стороны должны быть положительными')
        if cathetus[0] >= cathetus[1] + cathetus[2] or cathetus[1] >= cathetus[0] + cathetus[2] or cathetus[2] >= cathetus[1] + cathetus[0]:
            raise Exception ('Не треугольник')


