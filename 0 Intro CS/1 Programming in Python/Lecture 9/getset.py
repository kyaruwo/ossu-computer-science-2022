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


a = Animal(69)

# </> BEST to use getters and setters methods </>

# write
a.set_name("namae")

# access
print(a.get_age())
print(a.get_name())


# the way is above, below is shit style


#
# <!> not recommended, shit style <!>
# print(a.age) # access
# a.age = "infinite" # write
# a.size = "beeg" # create
# <!> not recommended, shit style <!>
#
