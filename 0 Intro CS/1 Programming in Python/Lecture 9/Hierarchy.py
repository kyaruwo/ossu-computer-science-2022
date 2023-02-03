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
    # overrides Animal __str__
    def __str__(self):
        return f"cat: {self.name}:{self.age}"

    # additional methods

    def speak(self):
        print("meow")


class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def __str__(self):
        return f"person: {self.name}:{self.age}"

    # additional methods

    def get_friends(self):
        return self.friends

    def add_friends(self, lname):
        if lname not in self.friends:
            self.friends.append(lname)

    def speak(self):
        print("wah")

    def age_diff(self, other):
        diff = self.age - other.age
        print(f"{abs(diff)} year difference")


class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def __str__(self):
        return f"student: {self.name}:{self.age}:{self.major}"

    # additional methods

    def change_major(self, major):
        self.major = major

    def speak(self):
        import random
        r = random.random()

        if r < 0.25:
            print("i have home work")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i shoud eat")
        else:
            print("i am watching tv")


class Rabbit(Animal):

    # class variables and their values
    # are shared between all instances of the class
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        # but instance variables and their values are not
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def __str__(self):
        return f"rabbit:{self.rid}"

    def __add__(self, other):
        return Rabbit(0, self, other)

    def get_rid(self):
        return str(self.rid).zfill(4)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __eq__(self, other):
        # get parent rabbit id's
        (p1rid, p2rid) = (self.parent1.rid, self.parent2.rid)
        (op1rid, op2rid) = (other.parent1.rid, other.parent2.rid)

        same_parent = p1rid == op1rid and p2rid == op2rid
        same_opposite_parent = p1rid == op2rid and p2rid == op1rid
        return same_parent or same_opposite_parent


r1 = Rabbit(1)
r2 = Rabbit(1)

r3 = Rabbit(0, r1, r2)
r4 = Rabbit(0, r2, r1)

r5 = Rabbit(0, r3, r4)
r6 = Rabbit(0, r4, r3)

print(r1, r2, r3, r4, r5, r6)

print(r3 == r4, r5 == r6)

print(r3 == r5, r3 == r6, r4 == r5, r4 == r5)
