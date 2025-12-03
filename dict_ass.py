#1 Create a dictionary called `student` with keys "name", "age", and "grade", and corresponding values "John", 20, and "A". Access and print the value of "name".
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
#2 Create a dictionary called `product` with keys "name", "price", and "stock", and corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
product = {"name": "Laptop", "price": 999.99, "stock": 50}
product["price"] = 899.99
print(product["price"])
#3 Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
employe = {"name": "Alice", "position": "Manager"}
employe["salary"] = 50000
print(employe)
#4 Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
inventory = {"apple": 10, "banana": 5, "orange": 8}
del inventory["banana"]
print(inventory)
#5 Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
person = {"name": "Bob", "age": 23, "city": "New York"}
person_copy = person.copy()
print(person_copy)
#6 Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
family = {
    "child1" : {"name": "blessing","age": 100 },
    "child2": {"name": "philip","age": 200},
    "child3": {"name": "sarah","age": 40  }
    }
print(family["child2"][1]["age"])

#7 Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car["model"])

#8 Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings = { "volume": 50, "brightness": 75, "language": "English"}
settings["language"] = "Spanish"
print(settings)

#9 Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
scores = {"math": 90, "science": 85, "english": 88}
del scores["science"]
print(scores)
#10 Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream" }
print("Appetizer" in menu)
#11 Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
config = {"theme": "dark", "language": "English", "timezone": "UTC"}
config.clear()
print(config)
#12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
phone_book = {"Alice": "0814789324", "Bob": "07065002347","charlie": "08081418142"}
print(phone_book.keys())
#13. Create a dictionary called `grades` with keys "math", "science", and "history", and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
grades = {"math": "A", "science": "B", "history": "C"}
print(grades.keys())
#14. 	Create a dictionary called `employee` with keys "name", "position", and "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
employee = {"name": "David", "ppsition": "Engineer", "salary": 70000}
print(employee.values())
#15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
print(game)

# ---------------------------------------------------------PART 2-------------------------------------------------------------------------------------------------
# Access and print the name of the teacher of "class2".
school = {
    "class1": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "class2": {
        "students": ["Charlie", "David"],
        "teacher": "Ms. Johnson"
    }
}
print(school["class2"]["teacher"])

# Access and print the second employee in the "Engineering" department.
company = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"]
}
print(company["Engineering"][1])

# Access and print the name of the second assistant.
university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"]
    },
    "students": ["John", "Jane", "Alice", "Bob"]
}
print(university["faculty"]["assistants"][1])

#  4.	Access and print the price of the third fruit.
store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5}
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4}
    ]
}
print(store["fruits"][2]["price"])

#  5. 	Access and print the second non-fiction book.
library = {
    "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
}
print(library["non-fiction"][1])

#  6. 	Access and print the age of the first child.
family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
print(family["children"][0]["age"])

#  7.	Access and print the name of the second main course.
restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"]
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
}
print(restaurant["menu"]["main_courses"][1])

#  8. 	Access and print the department of the user of the first desk.
workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"}
    ],
    "equipment": {"computers": 20, "printers": 10}
}
print(workspace["desks"][0]["department"])

#  9. 	Access and print the name of the second designer.
team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"]
}
print(team["designers"][1])

# 10. 	Access and print the second international destination.
travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
{"flights": 1500, "hotels": 2000}}
print(travel["international"][1])





