# first_name = "Ada"
# last_name = "Lovelace"
# print(first_name + " " + last_name)

# age = 25
# print(str(age) + " years old")

# name = "Alice"
# height = 1.68
# print( name + " is " + str(height) + " meters tall")

# is_hungry = True
# print("Is Alice hungry? " + str(is_hungry) + ".")

# city = "Paris"
# temperature = 22.5
# print("The temperature in " + city + " is " + str(temperature) + "°C")

# name = "John"
# age = 30
# married = False
# print(name + " is " + str(age) + " years old. Married: " + str(married))

# x = 4
# y = 5
# add = x + y
# print("The sum of " + str(x) + " and " + str(y) + " is " + str(add))


a = int(input("enter a number: "))
b = int(input("enter another number: "))

def add_2_numbers():
    global a 
    global b
    result = a + b
    print(result)

add_2_numbers()