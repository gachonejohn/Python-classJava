#a class
class Fruits:
    #a constructor method
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

    #normal method
    def display(self):
        print(f"I like eating {self.name}. it costs {self.price} and it is {self.color} in color")

# instance of a class /object
myobj = Fruits("apple",20,"red")
myobj.display()
myobj2 = Fruits("banana",10,"yellow")
myobj2.display()