class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return f"animal: {self.name}:{self.age}"

    # methods

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        assert type(new_age) == int, "integer only"
        self.age = new_age

    def get_name(self):
        return self.name

    def set_name(self, new_name=""):
        assert type(new_name) == str, "string only"
        self.name = new_name


class Cat(Animal):
    pass


# 23:00
# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-9-python-classes-and-inheritance/
