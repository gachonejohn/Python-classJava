# create a program that checks if a number is odd or even
# if else statement
num = int(input("Enter the number to check if is even or odd: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# create a program that checks if a person is eligible to vote based on age
age = int(input("Enter your age to check if you can vote: "))

if age >= 18:
    print(f"yes for {age} years, you are allowed to vote")
else:
    print(f"Sorry at {age} years, you are not allowed to vote")


# create a program that checks a student grade from the input marks
grade = int(input("Enter your Marks: "))

if 100 >= grade >= 85:
    print("your got: A")
elif 84 >= grade >= 60:
    print("your got: B")
elif 59 >= grade >= 40:
    print("your got: C")
elif grade <40:
    print("your got: D")
else:
    print("Invalid input")