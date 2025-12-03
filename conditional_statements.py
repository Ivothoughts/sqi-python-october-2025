# is_raining = True

# if is_raining:
#     print("Carry an umbrella")
# else:
# 	print("Enjoy the weather")


# num1 = 18
# num2 = 10

# if num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is not less than {num2}") 




# 1. Ask the user for a number. Print "It is even" if the number they entered is even.
# Otherwise, print "It is odd".

# num = int(input("Enter a number to check if it is even or odd: "))

# if num % 2 == 0:
#     print("It is even")
# else:
#     print("It is odd")
    

# 2. Ask the user for their name. If their name starts with "A", print "Your name starts with A",
# Otherwise, print, "Your name does not start with A".

# name = input("Enter your name: ")

# if name.lower().startswith("a"):
#     print("Your name starts with A")
# else:
#     print("Your name does not start with A")


# name = input("Enter your name: ")

# Case 1
# if name[0] == "A" or "a":  # python gotcha
# if name[0] == "A" or "a":
# if (name[0] == "A") or "a":  Sade
# if (name[0] == "A") or "a":
# if False or "a":
# if "a":
# if True:

# Case 2
# if (name[0] == "A") or "a":  Ade
# if (name[0] == "A") or "a":
# if False or "a":
# if "a":
# if True:

# Case 3
# if (name[0] == "A") or "a":  ade
# if (name[0] == "A") or "a":
# if False or "a":
# if "a":
# if True:


# if name[0] == "A" or name[0] == "a":
#     print("Your name starts with A")
# else:
#     print("Your name does not start with A")


# if name[0] in ["a", "A"]:
# if name[0] in "Aa":
#     print("Your name starts with A")
# else:
#     print("Your name does not start with A")
    

# temp = 1_000_000_000_000_000
# print(temp)


# if temp <= 0:
#     print("The weather is freezing")
# elif temp > 0 and temp < 100:
#     print("It is not yet boiling")
# elif temp == 100:
#     print("the water is boiling")
# else:
#     print("The water is above its normal boiling point")



# Ask the user for their score and tell them their grade

# equal to 0 or less than 40 - F
# greater than or equal to 40 and less than or equal to 45 - E
# greater than or equal to 46 and less than 50 - D
# greater than or equal to 50 and less than 59 - C
# greater than or equal to 60 and less than 69 - B
# greater than or equal to 70 and less than or equal to 100 - A


# temp = 1_000_000_000_000_000
# print(temp)


# if temp <= 0:
#     print("The weather is freezing")
# elif temp > 0 and temp < 100:
#     print("It is not yet boiling")

# if temp == 100:
#     print("the water is boiling")
# else:
#     print("The water is above its normal boiling point")


# name = "Eddy"
# if name == "Ed":
#     print("Ed")
# elif name == "Edd":
#     print("Edd")
# elif name == "Eddy":
#     print("Eddy")
# else:
#     print("Stranger")




# has_raincoat = True
# has_umbrella = True

# # If the person has either a raincoat or an umbrella, print "You are protected from the rain"
# # Otherwise, if the person has both a raincoat and an umbrella, print "You have double protection from the rain"
# # Otherise, print "You are NOT protected from the rain"

# if has_raincoat and has_umbrella:
#     print("You have double protection from the rain")
# elif has_raincoat or has_umbrella:
#     print("You are protected from the rain")
# else:
#     print("You are not protected from the rain")



# name = input("Enter your name: ").strip()


# # if not name:
# #     print("Hello Anonymous")
# # else:
# #     print(f"Hello, {name}")


# if name:
#     print(f"Hello, {name}")
# else:
#     print("Hello Anonymous")

# num = -190

# if num:
#     print("X")
# else:
#     print("Y")


# num = False


# if num == 0:
#     print("num is zero")

# if not num:
#     print("Num is falsy")
# else:
#     print("Num is truthy")

# husband = None  # null
# husband = ""  # blank

# husband = None

# if husband is None:
#     print("No husband")
# else:
#     print("Has husband")

# husband = None

# if husband is None: print("No husband")
# else: print("Has husband")


# Ternary operator

# husband = None
# print("No husband" if husband is None else "Has husband")
# print("No husband") if husband is None else print("Has husband")


# is_male = False
# gender = "He" if is_male else "She"
# print(gender)





# age = 12
# is_male = True


# if is_male:
#     if age < 18:
#         print("You are underage, cannot vote")
#     else:
#         print("You can vote")
# else:
#     print("Women cannot vote")



# if True:
#     pass

# print("End of file")



# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".