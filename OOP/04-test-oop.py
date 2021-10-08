class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(x):
        if isinstance(x, (int, float)):
            return True
        return False

    @property
    def coords_x(self):
        print("Вызов __get_coords_x")
        return self.__x

    @coords_x.setter
    def coords_x(self, x):
        print("Вызов __set_coords_x")
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    @coords_x.deleter
    def coords_x(self):
        print("вызов __del_coord_x")
        del self.__x

    # coordX = property(__get_coords_x, __set_coords_x, __del_coord_x)


pt = Point(1, 2)
print(pt.__dict__)

pt.coords_x = 7
x = pt.coords_x
print(pt.__dict__, x)

del pt.coords_x
print(pt.__dict__, x)
print(*Point.__dict__, sep='\n')
