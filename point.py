import math


class Point():
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

    def distance_to(self, point) -> float:
        return math.sqrt((self.__x - point.x)**2 + (self.__y - point.y)**2)
