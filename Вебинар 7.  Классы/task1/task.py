# Я не совсем понял прикол, вроде задание и вебинар по классам, но они уже созданы тут и
# нужно просто написать логику, хотя логичнее с нуля писать и создание класса и создание методов
class Segment:
    def __init__(self, first_point, second_point):
        self.a = first_point
        self.b = second_point

    def length(self):
        """Вычисление длины отрезка"""
        c = ((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2) ** (1 / 2)
        return round(c, 2)

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        return self.a[1] * self.b[1] <= 0

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        return self.a[0] * self.b[0] <= 0
