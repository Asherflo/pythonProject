class Animal:
    def __init__(self, name,age = 0):
        self.name = name
        self.age = age


    def speak(self):
        return "Animal speak"


class Dog(Animal):
    def __init__(self, name, type_, age):
        print("From Dog")
        super().__init__(name, age)
        self.type = type_


class Cat(Animal):
    pass

class Bingo(Dog,Cat):
    pass



dog = Dog("bingo", "Y",0)
cat = Cat("kitten")

print(dog.name)

print(dog.type)
print(dog.speak())
print(cat.name)
print(f"my name is {dog.name} and i  ")
