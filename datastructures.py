# list, index, an index value in a list is mutable(can be changed)

cars = ["Toyota", "BMW", "Subaru", "VW",]

print(cars)

# working with index
print(f"I love driving {cars[1]}") #this will print BMW

# The value can be changed
cars[2] = "Mazda" #index 2 has changed(mutable) from 'Subaru' to 'Mazda'
print(cars[2])

#sorting-- arranging alphabetically
cars.sort()
print(cars)

num = [5,6,3,0,2,-4,-7,-9,11,12,-17]
num.sort() #arranging from the lowest to the highest
print(num)



#tuple, indexed,immutable(can not be changed)
fruits=("mangoes","banana","Apple","mangoes")
print(fruits)

#set --unordered, no index
color = {"yellow","blue","green","white"}
print(color)

#dictionaries
employees = {"name":"John","age":21,"salary":100000}
print(employees)

print(f"The age of {employees['name']} is {employees['age']}")