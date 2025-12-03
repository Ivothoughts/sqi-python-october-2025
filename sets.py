#                    Mutable             Ordered         Indexed             Allow Duplicates
# 1. Strings           No                  Yes              Yes                     Yes
# 2. Lists             Yes                  Yes             Yes                     Yes
# 3. Tuples             No                  Yes             Yes                     Yes
# 4. Dicts              Yes           Yes, from Py 3.7+  Yes, but with keys Duplicate vals, but not duplicate keys
# 5. Sets               Yes                No               No                      No




# my_dict = {"language": "Spanish", "app": "Duolingo", "app": "Preply"}
# my_dict = {"language": "Spanish", "app": "Duolingo", "application": "Duolingo"}

# print(my_dict)


# my_set = {"language", "app", "app"}
# print(type(my_set))
# print(my_set)


# favorite_nums = {7, 12, 78, 14}
# print(favorite_nums[0])

# print(favorite_nums)

# -----------------------------------------------------------------------------

# countries = {"Nigeria", "Iraq", "Ghana", "Afghanistan", "Iraq", "Pakistan", "Russia", "North Korea"}

# print(len(countries))
# print(type(countries))


# data = {"James", 12, True, 1.75}


# shopping_list = ["rice", "beans", "oil", "maggi", "pepper", "maggi"]
# print(shopping_list)


# shopping_set = set(shopping_list)
# print(shopping_set)




# ---------------------------------ADDING TO A SET-----------------------------------------

# yam_foods = {"Yam and Egg", "Pounded Yam", "Yam Chips", "Yamarita", "Yam Porridge", "Fried Yam"}
# # yam_foods.add("Water Yam")
# yam_foods.add(["Water Yam", "Ojojo"])
# print(yam_foods)


# my_set = {[1, 2], [3, 4]}
# my_set = {[1, 2]: ["one", "two"], [3, 4]: ["three", "four"]}

# my_set = {{"item1", "item2"}, {"item3", "item4"}}


# import hashlib

# print(hashlib.sha256("PAssword123".encode()).hexdigest())

# print(hash("PAssword123"))



# yam_foods = {"Yam and Egg", "Pounded Yam", "Yam Chips", "Yamarita", "Yam Porridge", "Fried Yam"}

# yam_foods.update({"Yam and Stew", "Ojojo"})
# yam_foods.update(["Yam and Stew", "Ojojo"])
# yam_foods.update("Yam and Stew")
# yam_foods.update({"Yam and Stew": 4, "Ojojo": 5})
# yam_foods.update({"Pounded Yam"})

# yam_foods = yam_foods.union({"Yam and Stew", "Ojojo"})
# all_yam_foods = yam_foods.union({"Yam and Stew", "Ojojo"})

# print(yam_foods)
# print(all_yam_foods)



native_names = {"Omoseeke", "Atinuke", "Musa", "Asake", "Ayinla", "Adio", "Alake", "Akwuugo", "Osage", "Onome", "Ivie", "Ovie"}
more_native_names = {"Nkiruka", "Idriss", "Yerima" "Chinenye", "Feyi", "Onyinyechi", "Ngozi", "Chinaza", "Olusegun"}
# even_more_native_names = ["Seyi", "Gbenga", "Ajoke", "Omolabake", "Adedoyin", "Chijioke"]
even_more_native_names = {"Seyi", "Gbenga", "Ajoke", "Omolabake", "Adedoyin", "Chijioke"}

# seyi, gbenga, ajoke, labake, doyin, chijioke = even_more_native_names

# print(seyi)
# print(gbenga)
# print(ajoke)
# print(labake)

# all_names = native_names.union(more_native_names).union(even_more_native_names)
# native_names.update(more_native_names)
# native_names.update(even_more_native_names)
# print(native_names)

# caveat
# all_names = native_names | even_more_native_names | more_native_names

# print(all_names)
# ---------------------------------ADDING TO A SET-----------------------------------------

# ---------------------------------INTERSECTION OF SETS-----------------------------------------


# fruits = {"apple", "banana", "cherry"}
# brands = {"apple", "microsoft", "google"}
# flavors = {"strawberry", "apple", "mango", "vanilla"}


# fruits = fruits.intersection(brands).intersection(flavors)
# print(fruits)

# fruits.intersection_update(brands)
# fruits.intersection_update(flavors)
# print(fruits)


# fruits.intersection_update(brands)
# strings_in_common = fruits.intersection(brands)
# print(fruits)
# print(strings_in_common)


# fruits = {"apple", "banana", "cherry"}
# brands = {"apple", "microsoft", "google"}
# flavors = {"strawberry", "apple", "mango", "vanilla"}
# # fruits = fruits & brands & flavors
# fruits = fruits.intersection(brands).intersection(flavors)

# print(fruits)



# ---------------------------------INTERSECTION OF SETS-----------------------------------------



# ---------------------------------SYMMETRIC DIFFERENCE-----------------------------------------

# fruits = {"apple", "banana", "cherry"}
# brands = {"apple", "microsoft", "google"}
# # flavors = {"strawberry", "apple", "mango", "vanilla"}

# fruits.symmetric_difference_update(brands)
# print(fruits)



# nums1 = {45, 89, 78, 2, 76, 19, 34}
# nums2 = {45, 19, 78, 22, 76, 9, 34}
# # print(nums1.symmetric_difference(nums2))  # 89, 2, 22, 9

# nums1.symmetric_difference_update(nums2)
# print(nums1)


# fruits = {"apple", "banana", "cherry"}
# brands = {"apple", "microsoft", "google"}

# # banana, cherry, microsoft, google
# flavors = {"strawberry", "apple", "mango", "vanilla"}
# print(fruits.symmetric_difference(brands).symmetric_difference(flavors))

# banana, cherry, microsoft, google, strawberry, mango, vanilla



# fruits = {"apple", "banana", "cherry"}
# brands = {"microsoft", "google"}
# flavors = {"strawberry", "apple", "mango", "vanilla"}
# print(fruits.symmetric_difference(brands).symmetric_difference(flavors))


# fruits = {"apple", "banana", "cherry"}
# brands = {"microsoft", "google"}
# flavors = {"strawberry", "apple", "mango", "vanilla"}
# # flavors = ["strawberry", "apple", "mango", "vanilla"]
# # symmetric_difference = fruits.symmetric_difference(brands).symmetric_difference(flavors)
# # print(symmetric_difference)

# symmetric_difference = fruits ^ brands ^ flavors  # caret
# print(symmetric_difference)

# ---------------------------------SYMMETRIC DIFFERENCE-----------------------------------------


# ---------------------------------DIFFERENCE-----------------------------------------

# fruits = {"apple", "banana", "cherry"}
# brands = {"microsoft", "google", "apple"}

# fruits.difference_update(brands)
# print(fruits)

# print(fruits.difference(brands))

# print(fruits - brands)

# print(brands - fruits)



# nums1 = {4, 9, 1, 14}
# nums2 = {9, 12, 1, 8, 3}
# # print(nums1 - nums2)
# print(nums2 - nums1)  # 12, 8, 3

# ---------------------------------DIFFERENCE-----------------------------------------


# ---------------------------------REMOVING FROM A SET-----------------------------------------

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("cherry")
# print(fruits)

# fruits[0]
# del fruits["cherry"]


# fruits = {"apple", "banana", "cherry"}
# popped_fruit = fruits.pop()
# print(fruits)
# print(popped_fruit)


# fruits = {"apple", "banana", "cherry"}
# fruits.remove("mango")  # fails loudly
# print(fruits)


# fruits = {"apple", "banana", "cherry"}
# fruits.discard("mango")  # fails silently
# print(fruits)





# ---------------------------------REMOVING FROM A SET-----------------------------------------


# ---------------------------------MISCELLANEOUS-----------------------------------------

# fruits = {"apple", "banana", "cherry"}
# brands = {"microsoft", "google", "apple"}

# print(fruits.isdisjoint(brands))


# fruits = {"apple", "banana", "cherry"}
# brands = {"microsoft", "google", "lenovo"}

# print(fruits.isdisjoint(brands))


# print("google" in brands)
# print("google" in fruits)


# nums = {3, 7, 1, 38, 9, 4, 287, 0, 4}

# nums2 = {1, 0, 4}

# print(nums2.issubset(nums))
# print(nums.issuperset(nums2))

# print(nums.union(nums2))


# print({0, False})
# print({1, True, 2, 67, 2})
# print({True, 1, 2, 67, 2})




# ---------------------------------MISCELLANEOUS-----------------------------------------