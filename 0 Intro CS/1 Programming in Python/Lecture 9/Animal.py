class Animal(object):
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def __str__(self):
        return f"animal: {self.age}:{self.color}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(age, color)
        self.name = name

    def __str__(self):
        return f"cat: {self.name}, {super().__str__()[8:]}"


class Rabbit(Animal):
    def __init__(self, age, color):
        super().__init__(age, color)

    def __str__(self):
        return f"rabbit: {super().__str__()[8:]}"


# Cat

kuro = Cat("kuro", 1, "black")
shiro = Cat("shiro", 2, "white")
tyairo = Cat("tyairo", 0, "brown")

print(kuro)
print(shiro)
print(tyairo)

# Rabbit

rabbit1 = Rabbit(1, "black")
rabbit2 = Rabbit(2, "white")
rabbit3 = Rabbit(3, "brown")


print(rabbit1)
print(rabbit2)
print(rabbit3)
