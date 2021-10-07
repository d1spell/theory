class Point:

    # Инициализация приватных атрибутов
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    # Сеттер приватных атрибутов
    def setCoords(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Числа должны быть координатами')

    def getCoords(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.setCoords(3, 4)
print(pt.getCoords())
