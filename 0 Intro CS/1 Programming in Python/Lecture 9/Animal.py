class Animal(object):
    def __init__(self, age, color):
        self.age = age
        self.color = color


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(age, color)
        self.name = name


class Rabbit(Animal):
    def __init__(self, age, color):
        super().__init__(age, color)


# Cat

kuro = Cat("kuro", 1, "black")
shiro = Cat("shiro", 2, "white")
tyairo = Cat("tyairo", 0, "brown")


def cat_info(cat=Cat(None, None, None)):
    return cat.name, cat.age, cat.color


print(cat_info(kuro))
print(cat_info(shiro))
print(cat_info(tyairo))

# Rabbit

rabbit1 = Rabbit(1, "black")
rabbit2 = Rabbit(2, "white")
rabbit3 = Rabbit(3, "brown")


def rabbit_info(rabbit=Rabbit(None, None)):
    return rabbit.age, rabbit.color


print(rabbit_info(rabbit1))
print(rabbit_info(rabbit2))
print(rabbit_info(rabbit3))
