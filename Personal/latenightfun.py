class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog('Miles', 12)

print(buddy.name)


