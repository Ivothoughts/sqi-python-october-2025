# 1. Print the second and second-to-last items in the list.
# Input: animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
# Expected Output:
# cat
# sheep
animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
print(animals[1])
print(animals[-2])

# 2. Replace the first and last items with "lion" and "elephant", then print the list.
# Input: animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
# Expected Output:
# ['lion', 'cat', 'goat', 'cow', 'sheep', 'elephant']

animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
animals.remove("dog")
animals.insert(0, "lion")
animals.remove("horse")
animals.append("elephant")
print(animals)

# 3. Add "pig" to the list and then insert "hen" at index 2.
# Input: animals = ["dog", "cat", "goat"]
# Expected Output:
# ['dog', 'cat', 'hen', 'goat', 'pig']

animals = ["dog", "cat", "goat"]
animals.append("pig")
animals.insert(2, "hen")
print(animals)

# 4. Remove "cow" from the list and print the updated list.
# Input: animals = ["dog", "cat", "cow", "goat", "sheep"]
# Expected Output:
# ['dog', 'cat', 'goat', 'sheep']

animals = ["dog", "cat", "cow", "goat", "sheep"]
animals.remove("cow")
print(animals)

# 5. Check if "goat" is in the list and print the result.
# Input: animals = ["dog", "cat", "cow", "goat", "sheep"]
# Expected Output:
# True

animals = ["dog", "cat", "cow", "goat", "sheep"]
print("goat" in animals)

# 6. Combine two lists of foods and print the result.
# Input: list1 = ["rice", "beans"], list2 = ["yam", "plantain"]
# Expected Output:
# ['rice', 'beans', 'yam', 'plantain']

list1 = ["rice", "beans"]
list2 = ["yam", "plantain"]
print(list1 + list2)

# 7. Create a list of drinks and check if "water" exists.
# Input: drinks = ["tea", "coffee", "juice", "soda"]
# Expected Output:
# False
drinks = ["tea", "coffee", "juice", "soda"]
print("water" in drinks)

# 8. Add "water" and "milk" at once to the list.
# Input: drinks = ["tea", "coffee", "juice"]
# Expected Output:
# ['tea', 'coffee', 'juice', 'water', 'milk']

drinks = ["tea", "coffee", "juice"]
drinks.extend(["water", "milk"])

# 9. Replace "coffee" with "hot chocolate" and print the list.
# Input: drinks = ["tea", "coffee", "juice"]
# Expected Output:
# ['tea', 'hot chocolate', 'juice']

drinks = ["tea", "coffee", "juice"]
drinks[1] = "hot chocolate"
print(drinks)

# 10. Create a list of vehicles, add and remove some items step by step.
# Input: vehicles = ["car", "bike", "bus", "train"]
# Steps:
#   1. Add "boat" to the end
#   2. Insert "truck" at index 1
#   3. Remove "bike"
#   4. Check if "plane" exists
# Expected Output:
# ['car', 'truck', 'bus', 'train', 'boat']
# False

vehicles = ["car", "bike", "bus", "train"]
vehicles.append("boat")
vehicles.insert(1, "truck")
vehicles.remove("bike")
print(vehicles)
print("plane" in vehicles)

# 11. Append "Abuja" to the end of the list.
# Input: cities = ["Lagos", "Kano", "Ibadan"]
# Expected Output:
# ['Lagos', 'Kano', 'Ibadan', 'Abuja']

cities = ["Lagos", "Kano", "Ibadan"]
cities.append("Abuja")
print(cities)

# 12. Extend the list with another list of cities.
# Input: cities = ["Lagos", "Kano"], more_cities = ["Abuja", "Enugu"]
# Expected Output:
# ['Lagos', 'Kano', 'Abuja', 'Enugu']

cities = ["Lagos", "Kano"]
more_cities = ["Abuja", "Enugu"]
cities.extend(more_cities)
print(cities)
