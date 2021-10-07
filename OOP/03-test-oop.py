""" public, private,
    геттеры и сеттеры"""


class Point:
    CONST = 100  # Константа, изменения которой блокируются через перегрузку __setattr__

    def __init__(self, x=0, y=0):
        self.__x = x  # приватные
        self.__y = y  # атрибуты

    @staticmethod
    def __check_value(x):  # Проверка введеных координат на принадлежность к числовым типам
        if isinstance(x, (int, float)):
            return True
        return False

    def setCoords(self, x, y):  # изменение приватных атрибутов
        if self.__class__.__check_value(x) and self.__class__.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('<< Координаты должны быть числами >>')

    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Частная переменная'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'CONST':
            raise AttributeError
        else:
            self.__dict__[key] = value

    def getCoords(self):  # Получение приватных атрибутов
        return self.__x, self.__y


pt = Point(2, 4)
print(pt.getCoords())
pt.setCoords(3.6, 'r')
print(pt.getCoords())
print(pt.__dict__)

# pt.CONST = 'изменение константы'
