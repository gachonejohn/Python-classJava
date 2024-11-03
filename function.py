def john():
    print("my name is John")
john() #calling the function

def addtwonumbers():
    num = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum of {num} and {num2} is {num + num2}")
#using the above function in an external file called 'call'


# function with parameters
def javaclass(name,age,gender):
    print(f"student name: {name}, age: {age}, gender: {gender}")


def multiply_two_numbers(num1,num2):
    print(f"the product of the two numbers is", num1*num2)