# while loop --executes until the condition becomes false

num = 2

while num <=15:
    print(num)
    num += 1
    #incremental loop


# create a while loop that prints 100 to zero with a difference of 5 each

#solution
num2 = 100

while num2 >= 0:
    print(num2)
    num2 -= 5
    #decremental loop

# for loop
name = ["john", "liz", "alex", "Tom", "jane"]

for i in name:
    print(i)

# test calculating the sum of numbers in a for loop
num = [22,23,78,65,9,12,7,8,4]
total = 0
for n in num:
    total += n
print(total)

# using the above loop to print the even numbers in the 'num' list
evens= []
for x in num:
    if x % 2 == 0:
        evens.append(x)#pushing 'x' to the same list, pushing it after the previous one
        evens.sort() #arranging them in ascending order
print(evens)



