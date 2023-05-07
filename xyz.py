import math


class XYZ():
    def __init__(self, x_coord=0, y_coord=0):
        self.__x = x_coord
        self.__y = y_coord

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"{self.__x, self.__y}"

    def substract(self, point):
        return XYZ(self.__x - point.x, self.__y - point.y)

    def add(self, point):
        return XYZ(self.__x + point.x, self.__y + point.y)


class Point(XYZ):

    def distance_to(self, point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


class Vector(XYZ):

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        return Vector(self.x/self.length, self.y/self.length)
