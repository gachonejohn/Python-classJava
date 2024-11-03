# create a class called person with name,age,gender
#as the attributes
#have a constructor method,normal method and three objects

#class
class Person:
    #constructor
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #normal
    def show(self):
        print(f"This is {self.name}, {self.age} years old, and is a {self.gender}")


#objects
obj1 = Person("John",23,"Male")
obj1.show()
obj2 = Person("Liz",21,"Female")
obj2.show()
obj3 = Person("Peter",19, "Male")
obj3.show()