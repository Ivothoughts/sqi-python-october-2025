# number = int(input("Enter any number of your choice:"))
# # is_even = number % 2 == 0
# if number % 2 == 0:
#     print("It is even")
# else:
#     print("It is odd")


# name = input("What is your name:")
# # starts_with = name.lower().startswith("a")
# if name.lower().startswith("a"):
#     print("Your name starts with A")
# else:
#     print("Your name does not start with A")


# score = int(input("Enter your score: "))
# if score < 0:
#     print( "score can not be negative")
# elif score == 0 or score <= 40:
#     print("Your grade is F")
# elif score >= 40 and score <= 45:
#     print("your grade is E")
# elif score >= 46 and score <= 50:
#     print("your grade is D")
# elif score >= 50 and score <= 59:
#     print("your grade is C")
# elif score >= 60 and score <= 69:
#     print("your grade is B")
# elif score >= 70 and score  <= 100:
#     print("your grade is A")
# elif score > 100:
#     print("Invalid score or score can not exceed 100")

# has_raincoat = False
# has_umbrella = False

# if has_raincoat and has_umbrella:
#     print("You have double protection")
# elif has_raincoat or has_umbrella:
#     print("You are protected from the rain")
# else:
#     print("You are not protected from the rain")
    

mode = input("what mode is activated: ").lower()
if mode == "manual":
    print("Manual mode is activated")
elif mode == "automatic":
    print("Automatic mode activated")
elif mode == "off":
    print("system is Off")
else:
    print("The mode is Invalid")







