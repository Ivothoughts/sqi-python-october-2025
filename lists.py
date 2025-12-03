#                       Indexed             Mutable         Duplicates      Ordered
# Strings                Yes                  No              Yes            Yes
# Lists                  Yes                  Yes             Yes            Yes


# foods = ["yam", "beans", "rice", "plantain", "spaghetti"]
# print(foods[0])
# print(foods[-1])

# foods[-1] = "macaroni"
# print(foods)


# foods = ["yam", "beans", "rice", "plantain", "rice", "spaghetti"]
# print(foods)
# foods = {"yam", "beans", "rice", "plantain", "rice", "spaghetti"}
# print(foods)

# inventory = {"yam": 5, "beans": 2, "plantain": 10, "rice": 5}
# print(inventory)


# shopping_list = ["spaghetti", "tomatoes", "liver", "groundnut oil", "seasoning", "spices", "pepper", "cinnamon"]
# print(shopping_list)


# print("seasoning" in shopping_list)

# shopping_list[2] = "chicken"
# print(shopping_list)

# shopping_list.append("onions")
# shopping_list.extend(("ginger", "garlic"))
# shopping_list.extend(("ginger",))
# shopping_list.extend(["ginger"])

# shopping_list.insert(2, "garlic")
# shopping_list.insert(0, "garlic")

# shopping_list.append("crayfish")
# shopping_list.remove("liver")
# print(shopping_list)

# list methods work in-place

# name = "Deji"
# name = name.upper()
# print(name)


# means_of_transport
# Create a list called means_of_transport containing the following means of transport:
# car, lorry, camel, ship, canoe 

# 1. Add "plane" to the end
# 2. Add "jet" inbetween "lorry" and "camel"
# 3. Check if "helicopter" is in the list
# 4. Remove "canoe" from the list
# 5. Change "lorry" to "van"
# 6. Add "helicopter" and "broom" at the same time to the list



# ------------------------------LIST SLICING---------------------------------------

# sports = ["Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey"]

# print(sports[1:4])
# print(sports[1][3:6])
# print(sports[3][2:])
# print(sports[2][4:])

# sports[3] = "Skating"
# print(sports[1:4])
# print(sports[1:2])
# sports[1:4] = ["Skating"]
# sports[3] = ["Skating"]
# sports[2:] = ["Baseball", "Badminton"]
# print(sports)

# ------------------------------LIST SLICING---------------------------------------

# ------------------------------MISCELLANEOUS---------------------------------------
# sports = ["Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey"]
# print(sports)
# print(len(sports))
# print(type(sports))  # <class 'list'>

# sports = ("Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey")
# print(type(sports))
# sports = list(sports)
# print(type(sports))

# name = "David"
# # print(list(name))
# # name = list(name)
# # name_list = list(name)
# print(name)


# my_list = ["Bello", 3, 8.9, True, None]
# print(my_list)

# even_nos = [4, 8, 12, 6, 2]

# ------------------------------MISCELLANEOUS---------------------------------------


# ------------------------------REMOVING FROM A LIST---------------------------------------
# even_nos = [4, 8, 12, 6, 2, 12]
# even_nos.remove(12)
# even_nos.remove(12)
# print(even_nos)


# even_nos = [4, 8, 12, 6, 2, 12]
# # even_nos.pop()
# # even_nos.pop(2)
# popped_num = even_nos.pop(-3)
# print(even_nos)
# print(popped_num)

# sports = ["Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey"]
# # popped_sport = sports.pop(3)
# popped_sport = sports.pop(100)
# print(sports)

# print(popped_sport)

# sports = ["Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey"]
# del sports[-3]
# print(sports)


# sports = ["Tennis", "Volleyball", "Football", "Golf", "Basketball", "Hockey"]
# print(sports)
# del sports
# print(sports)  # NameError


# print(school_name)


# name = "Jane"
# del name
# print(name)
# ------------------------------REMOVING FROM A LIST---------------------------------------


# ------------------------------CLEAR A LIST---------------------------------------

# movies = ["Peaky Blinders", "End Game", "To kill a Monkey", "Devil is a Liar", "Monster", "Solo leveling", "Zootopia", "Barbie"]
# movies.clear()
# movies = []
# print(movies)


# ------------------------------CLEAR A LIST---------------------------------------



# ------------------------------SORTING A LIST---------------------------------------

movies = ["Peaky Blinders", "End Game", "To kill a Monkey", "Devil is a Liar", "Monster", "Solo leveling", "Zootopia", "Barbie"]
# movies.sort()
# movies.sort(reverse=True)
# print(movies)

# movies = ["Peaky Blinders", "End Game", "To kill a Monkey", "Devil is a Liar", "Monster", "Solo leveling", "Zootopia", "Barbie"]
# sorted_movies = sorted(movies)
# print(movies)
# print(sorted_movies)

# name = "blessing"
# print(sorted(name))
# print("".join(sorted(name)))


# names = ["Danny", "Daniel", "Dan", "Dante"]
# ["Daniel", "Danny", "Dan", "Dante"]
# ["Daniel", "Dan", "Danny", "Dante"]
# ["Dan", "Daniel", "Danny", "Dante"]
# names.sort()
# print(names)


# nums = [1, 10, 4]
# nums.sort()
# print(nums)


# nums = ["9", "10", "4"]  # lexicographically
# nums.sort()
# print(nums)

# nums = [57, 49, 52]

# nums = [9, 10, 4]
# nums.sort()
# print(nums)

# nums = ["9", "50", "4"]  # lexicographically
# nums.sort()
# print(nums)


# nums = ["10", "11", "19"]
# nums.sort()
# print(nums)


# nums = [89, 34, 289, 178, 23]
# nums.sort()
# print(nums)


# movies = ["Peaky Blinders", "End Game", "To kill a Monkey", "Devil is a Liar", "Monster", "Solo leveling", "Zootopia", "barbie"]
# # movies.sort()
# # movies.sort(key=str.lower)
# movies.sort(key=str.lower, reverse=True)
# print(movies)

# movies = ["Peaky Blinders", "End Game", "To kill a Monkey", "Devil is a Liar", "Monster", "Solo leveling", "Zootopia", "barbie"]
# print(sorted(movies, key=str.lower, reverse=True))


# ------------------------------SORTING A LIST---------------------------------------



# ------------------------------REVERSING A LIST---------------------------------------

# musicians = ["Davido", "Nathaniel Bassey", "Wizkid", "Hillsong", "Maverick Music", "GUC", "Ify Labels", "Frank Edwards", "Judikay", "Mercy Chinwo"]
# musicians.reverse()
# print(musicians)


# nums = [1, 2, 3]
# # nums.reverse()
# # print(nums)
# nums.sort(reverse=True)
# print(nums)


# nums = [2, 1, 3]
# # nums.reverse()
# # print(nums)  # 3, 1, 2
# nums.sort(reverse=True)
# print(nums)  # 3, 2, 1

# musicians = ["Davido", "Nathaniel Bassey", "Wizkid", "Hillsong", "Maverick Music", "GUC", "Ify Labels", "Frank Edwards", "Judikay", "Mercy Chinwo"]
# musicians = musicians[::-1]
# print(musicians)

# musicians = ["Davido", "Nathaniel Bassey", "Wizkid", 10, "Hillsong", "Maverick Music", "GUC", "Ify Labels", "Frank Edwards", "Judikay", "Mercy Chinwo"]

# musicians.sort()
# musicians = ["Davido", "Nathaniel Bassey", "Wizkid", "10", "Hillsong", "Maverick Music", "GUC", "Ify Labels", "Frank Edwards", "Judikay", "Mercy Chinwo"]

# musicians.sort()

# print(musicians)


# items = [True, 1, 12]
# items.sort()
# print(items)

# # items = [12.8, 1, 12]
# items = [12.0, 1, 12]  # 
# items.sort()
# print(items)
# ------------------------------REVERSING A LIST---------------------------------------



# ------------------------------COPY A LIST---------------------------------------

# import copy
# gadget_brands = ["Apple", "Itel", ["Tecno", "Samsung", "HP"], "Dell", "Lenovo", ["Haier Thermocool", "LG", "Snowsea"], "HiSense", "Toshiba", "Toyota"]

# gadget_brands_copy = gadget_brands.copy()

# print(id(gadget_brands))
# print(id(gadget_brands_copy))

# gadget_brands_copy = copy.copy(gadget_brands)
# gadget_brands_copy = copy.deepcopy(gadget_brands)
# print(id(gadget_brands[2]))
# print(id(gadget_brands_copy[2]))



# gadget_brands = ["Apple", "Itel", "Tecno", "Samsung", "HP", "Dell", "Lenovo", "Haier Thermocool", "LG", "Snowsea", "HiSense", "Toshiba", "Toyota"]
# gadget_brands_copy = copy.copy(gadget_brands)

# gadget_brands_copy.sort()

# print(gadget_brands)
# print(gadget_brands_copy)

# gadget_brands = ["Apple", "Itel", "Tecno", "Samsung", "HP", "Dell", "Lenovo", "Haier Thermocool", "LG", "Snowsea", "HiSense", "Toshiba", "Toyota"]
# gadget_brands_sorted = sorted(gadget_brands)

# print(gadget_brands)
# print(gadget_brands_sorted)

# ------------------------------COPY A LIST---------------------------------------

# ------------------------------JOIN LISTS---------------------------------------

# cars = ["Mitsubushi", "Ford", "Lexus", "Mercedes Benz", "Volkswagen", "Lamborghini", "Ferrari", "Rolls Royce"]
# more_cars = ["Tesla", "Jaguar", "Doge", "Chevrolet", "Nissan", "Beetle"]
# all_cars = []

# all_cars.extend(cars)
# all_cars.extend(more_cars)
# print(cars)
# print(more_cars)
# print(all_cars)


# all_cars = [*cars, *more_cars]
# print(all_cars)


# all_cars = cars + more_cars
# print(all_cars)

# print("; ".join(["Hello", "Hi"]))
# ------------------------------JOIN LISTS---------------------------------------


# ------------------------------NESTED LISTS---------------------------------------

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][1])
# print(matrix[-1][-1])

# print(matrix[0][0])

# matrix[2][1] = 18

# print(matrix)


# matrix[1][1] = matrix[1][0] + matrix[1][2]

# print(matrix)



nested_list = [
    ["Alice", "Bob"],
    [10, 20, 30],
    [True, False]
]

# print(nested_list[0][0][1:])

# nested_list[0].reverse()
# print(nested_list)
# print(nested_list[0])

# nested_list[1].append(50)
# print(nested_list)

nested_list[0][0] = nested_list[0][0][::-1]
nested_list[0][1] = nested_list[0][1][::-1]
print(nested_list)


# ------------------------------NESTED LISTS---------------------------------------