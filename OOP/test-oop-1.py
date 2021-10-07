# Объекты-свойства(Property)
class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def __getCoordX(self):
        return self.__x

    def __setCoordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    coordX = property(__getCoordX, __setCoordX)


pt = Point(1, 2)
pt.coordX = 100  # запись
x = pt.coordX  # чтение
print(x)
