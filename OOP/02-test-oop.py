class Point():

    def __init__(self, obj=None): #создание из другого объекта
        if obj:
            self.x = obj.x
            self.y = obj.y
        else:
            self.x = 0
            self.y = 0

    def get(self):
        return self.x, self.y


# testing
point_one = Point()
print(point_one.get())

point_one.x = 4
point_one.y = 6

point_two = Point(point_one)
print(point_two.get())
