#                       Mutable             Ordered         Indexed             Allow Duplicates
# 1. Strings              No                  Yes             Yes                   Yes
# 2. Lists                Yes                 Yes            Yes                    Yes
# 3. Tuples               No                  Yes             Yes                   Yes
# 4. Dicts                Yes              Yes (from 3.7+)  Yes, but with keys      Duplicate values, but not duplicate keys


# my_tuple = (1, 2, 2, 1, 3)
# # my_tuple[2] = 4
# print(my_tuple)
# print(my_tuple[2])



# phone_book = {"Ife": "08148548826", "Blessing": "07068454572", "Francis": "09028485066"}
# print(phone_book)


# print(phone_book["Blessing"])

# print(phone_book.get("Blessing"))

# # print(phone_book[1])

# # del phone_book["Francis"]
# # print(phone_book)

# phone_book["Sarah"] = "09078887535"
# print(phone_book)


# phone_book["Blessing"] = "08038299679"
# print(phone_book)


# print("Francis" in phone_book)
# print("Francis" in phone_book.keys())
# print(phone_book.keys())
# print(type(phone_book.keys()))
# print(list(phone_book.keys()))
# print("Francis" not in phone_book)


# print(phone_book.values())
# print("08148548826" in phone_book.values())

# print(phone_book.items())
# print(list(phone_book.items()))





# ages = [12, 76, 27, 43]
# print(sum(ages) / len(ages))


# students_and_ages = {"Ife": 12, "Blessing": 76, "Francis": 27, "Feyi": 43}
# print(min(students_and_ages, key=students_and_ages.get))


# yoruba_translator = {
#     "sit": ["joko"],
#     "stand": ["dide", "gbera"],
#     "broom": ["Igbale"],
#     "eat": ["jeun"],
#     "king": ["Oba"],
#     "child": ["omo"]
# }
# print(yoruba_translator)
# print(yoruba_translator["sit"][0])
# print(yoruba_translator["stand"][1])
# # print(yoruba_translator["king"])


# Create a dictionary called my_info
# It contains the following keys (put in your info as values): "name", "age", "gender", "dept"
# Print the value of "age"
# Change the value of "name" to your last name
# Remove the gender
# Check if 12 is an age in the dictionary
# Check if there is a key called "dept"
# Print all the keys of the dictionary as a list


# ----------------------------------------------------.GET()---------------------------------------------------------------

# my_dream_car = {
#     "brand": "BMW",
#     "model": "M Series",
#     "color": "Metallic Grey",
#     "year_manufactured": 2024,
#     "is_electric": "True",
# }

# print(my_dream_car["color"])  # square bracket notation
# print(my_dream_car.get("color"))  # .get() method


# # print(my_dream_car["tire_size"])
# print(my_dream_car.get("tire_size"))

# result = my_dream_car.get("tire_size", "Does not exist")
# print(result)

# print(my_dream_car.get("model"))

# ----------------------------------------------------.GET()---------------------------------------------------------------



# ----------------------------------------------------.SETDEFAULT()---------------------------------------------------------------

# my_dream_car = {
#     "brand": "BMW",
#     "model": "M Series",
#     "color": "Metallic Grey",
#     "year_manufactured": 2024,
#     "is_electric": "True",
# }

# print(my_dream_car.get("model_number"))
# print(my_dream_car.get("model_number", "N/A"))


# print(my_dream_car.setdefault("model_number"))
# print(my_dream_car)


# print(my_dream_car.setdefault("model_number", "N/A"))
# print(my_dream_car)

# print(my_dream_car.setdefault("color", "silver"))
# print(my_dream_car)

# ----------------------------------------------------.SETDEFAULT()---------------------------------------------------------------



# ----------------------------------------------------UPDATING A DICT---------------------------------------------------------------
my_dream_house = {
    "type": "castle",
    "no_of_rooms": 15,
    "color": "white",
    "location": "On an island"
}


# print(my_dream_house)
# my_dream_house["no_of_rooms"] = 20  # square bracket notation
# my_dream_house["has_garage"] = True  # square bracket notation
# print(my_dream_house)

# print(my_dream_house)
# my_dream_house.update(no_of_rooms=20, color="peach")  # kwargs
# print(my_dream_house)


# print(my_dream_house)
# my_dream_house.update(has_garage=True)  # kwargs
# print(my_dream_house)


# print(my_dream_house)
# # # my_dream_house.update(no of rooms=20, color="peach")  # error
# my_dream_house.update({"has garage": True, "no of neighbors": 5})  # kwargs
# print(my_dream_house)
# ----------------------------------------------------UPDATING A DICT---------------------------------------------------------------




# my_dict = {
#     1: "one",
#     (2, "two"): "TWO",
#     "1": 'one',
#     1.9: "one point nine",
#     # [3, "three"]: "THREE",
#     # {"hello": "hi"}: "something"
# }


# ----------------------------------------------------REMOVING FROM A DICT---------------------------------------------------------------

# my_info = {
#     "name": "Olaniyi Francis",
#     "complexion": "dark",
#     "is_male": True,
#     "occupation": "Crypto Trader",
#     "is_married": False
# }


# print(my_info)
# del my_info["occupation"]
# print(my_info)


# del my_info

# print(my_info)  # NameError

# print(my_info)
# is_married = my_info.pop("is_married")
# print(is_married)
# print(my_info)


# del my_info["OCCUPATION"]
# my_info.pop("OCCUPATION")

# if "OCCUPATION" in my_info:
#     del my_info["OCCUPATION"]
# print(my_info)
# if "occupation" in my_info:
#     del my_info["occupation"]

# print(my_info)



# print(my_info)
# print(my_info.popitem())
# print(my_info)


my_info = {
    "name": "Olaniyi Francis",
    "complexion": "dark",
    "is_male": True,
    "is_married": False,
    "occupation": "Crypto Trader",
}

my_work_info = {
    "active_hours": range(10, 2),
}
# print(my_info.popitem())
# occupation_key, occupation_val = my_info.popitem()

# my_work_info[occupation_key] = occupation_val

# print(my_work_info)


# key = "occupation"

# val = my_info.pop(key)

# my_work_info[key] = val

# print(my_work_info)
# ----------------------------------------------------REMOVING FROM A DICT---------------------------------------------------------------


# ----------------------------------------------------MISCELLANEOUS---------------------------------------------------------------

# hobby = {
#     "name": "Cooking",
#     "love_to_cook": "Spaghetti Bolognese",
#     "frequency": "everyday",
# }

# print(len(hobby))
# print(type(hobby))


# my_list = [2, 38, 902]
# # print(dict(my_list))


# # hobby = [("name", "Cooking"), ("love_to_cook", "Spaghetti Bolognese"), ("frequency", "everyday")]
# hobby = [["name", "Cooking"], ["love_to_cook", "Spaghetti Bolognese"], ["frequency", "everyday"]]
# print(dict(hobby))


# hobby = dict(name="Cooking", love_to_cook="Spaghetti Bolognese", frequency="everyday")
# print(hobby)


# ----------------------------------------------------MISCELLANEOUS---------------------------------------------------------------



# ----------------------------------------------------CLEAR A DICT---------------------------------------------------------------

# hobby = {'name': 'Cooking', 'love_to_cook': 'Spaghetti Bolognese', 'frequency': 'everyday'}
# # hobby.clear()
# hobby = {}
# print(hobby)

# my_set = {"james", "john", "jake", "janet"}
# my_dict = {}
# my_set = set()
# print(type(my_set))


# ----------------------------------------------------CLEAR A DICT---------------------------------------------------------------


# ----------------------------------------------------NESTED DICTs---------------------------------------------------------------




# ----------------------------------------------------NESTED DICTs---------------------------------------------------------------



