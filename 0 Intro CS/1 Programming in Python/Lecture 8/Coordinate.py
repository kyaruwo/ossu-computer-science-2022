from os import system as sys
sys("cls")


# class_defintion name/type(parent)
class Coordinate(object):
    # initialize some data attributes
    # use to create parameters
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # by default if you print(coordinate) you get its memory address
    # e.g <__main__.Coordinate object at 0x00000N69I420C69E>
    # we can make it more informative using the code below
    def __str__(self):
        return f"<{self.x}, {self.y}>"

    # methods
    def distance(self, other):
        # euclidean distance formula
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        distance = (x_diff_sq + y_diff_sq)**0.5
        return distance

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


origin = Coordinate(0, 0)
coord = Coordinate(42, 69)

# print() using __str__
print("origin :", origin)
print("coord :", coord)

# accessing attributes
print("origin :", origin.get_x(), origin.get_y())
print("coord :", coord.get_x(), coord.get_y())


# conventional way
print("distance :", coord.distance(origin))

# unconventional way, java hell :>
print("distance :", Coordinate.distance(coord, origin))


# isinstance()
print(isinstance(coord, Coordinate))
print(isinstance(42069, Coordinate))
