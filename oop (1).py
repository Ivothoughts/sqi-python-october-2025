# OOP - Object Oriented Programming

# Functional & Modular Programming

# OOP - Object and Class



# class BankAccount:
#     # magic dunder method
#     def __init__(self, bank_name: str, account_number: str, account_owner: str, balance: int, is_savings: bool):
#         self.bank_name = bank_name
#         self.account_no = account_number
#         self.account_owner = account_owner
#         self.balance = balance
#         self.is_savings = is_savings
#         # print("Something")
#         # print(is_savings)


#     def check_account_details(self):
#         return f"{self.account_owner}'s {self.bank_name} account. Account number - {self.account_no}."
    


# # print(str(4))

# # int()

# ife_bank_acct = BankAccount("GTBank", "0318497832", "Ife Omole", 3_200_000, False)
# sarah_bank_acct = BankAccount("Access Bank", "0788419919", "Sarah Omoseeke", 4_000_900, True)

# # print(BankAccount("Access Bank", "0788419919", "Sarah Omoseeke", 4_000_900, True))

# print(ife_bank_acct.account_no)
# print(ife_bank_acct.bank_name)
# print(ife_bank_acct.balance)
# print(ife_bank_acct.check_account_details())
# print(sarah_bank_acct.check_account_details())

# def greet():
#     return "Hello"


# print(greet())


# class Person:
#     def __init__(self, name, age, height, weight, is_male: bool, complexion, occupation):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.is_male = is_male
#         self.complexion = complexion
#         self.occupation = occupation


#     def introduce_yourself(self):
#         gender = "Male" if self.is_male else "Female"  # ternary operator
#         return f"My name is {self.name}. I am a/an {self.occupation}. I am a {gender}."
        

# towi = Person("Towi Iji", 30, 1.67, 56, False, "caramel", "student")

# print(towi.weight)
# print(towi.occupation)

# towi.occupation = "Software Engineer"

# print(towi.occupation)

# print(towi.introduce_yourself())






# is_male = True


# if is_male:
#     gender = "Male"
# else:
#     gender = "Female"



# gender = "Male" if is_male else "Female"

# Create a Car class that has the following attributes:
# - color: str
# - brand: str
# - model: str
# - year_manufactured: int
# - engine: str
# no_of_doors: int

# Create 3 objects out of the class
# The objects created out of the class should be able to move, reverse, honk




# -----------------------------------------ASSIGNMENT-----------------------------------------------
# 1. Create a class called Book with the following attributes:
#    - title
#    - author
#    - genre
#    - page_count
#    - year_published
#
#    The class should have a method called short_description() that returns:
#    "{title} by {author} ({year_published}), {genre}, {page_count} pages."
#
#    After defining the class, create 3 different Book objects with different values.
# ---------------------------------------------------------------------------------------------------

# class Book:
#     def __init__(self, title, author, genre, page_count, year_published):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.page_count = page_count
#         self.year_published = year_published

#     def short_description(self):
#         return f"{self.title} by {self.author} ({self.year_published}), {self.genre}, {self.page_count} pages."

# book1 = Book("The Notebook", "Nicholas Spark", "Romance", 800, 1986)
# book2 = Book("Atomic Habits", "James Clear", "Self-help", 123, 2018)
# book3 = Book("Things Fall Apart", "Chinua Achebe", "Fiction", 123, 1958)

# print(book1.author)

# print(book2.page_count)
# book2.page_count = 200
# print(book2.page_count)


# books: list[Book] = [book1, book2, book3]

# for book in books:
#     print(book.year_published)
#     print(book.short_description())


# -----------------------------------------ASSIGNMENT-----------------------------------------------
# 2. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.

# 3. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.

# class Student:
#     def __init__(self, name: str, age: int, grades: list[int]):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
    
#     def is_passing(self):
#         return True if self.average_grade() >= 50 else False
    



# Example usage:
# s1 = Student("Blessing Ezugwu", 26, [78, 65, 5, 89, 90])
# s2 = Student("Ife Omole", 22, [2, 100, 99, 51, 79, 32])

# print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# Expected Output:
# Alice average: 76.25 passing: True
# Bob average: 33.75 passing: False


# 4. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.


# class Playlist:
#     def __init__(self, name: str, songs: list[str]):
#         self.name = name
#         self.songs = songs

#     def add_song(self, song: str):
#         self.songs.append(song)

#     def total_songs(self):
#         return len(self.songs)
    
#     def show_songs(self):
#         return ", ".join(self.songs)


# # Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us


# 5. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.


# class ShoppingCart:

#     HAS_WHEELS = True

#     def __init__(self, owner, items: dict[str, int]):
#         self.owner = owner
#         self.items = items

#     def add_item(self, item, price):
#         self.items[item] = price

#     def total_cost(self):
#         return sum(self.items.values())
    
#     def most_expensive(self):
#         return max(self.items, key=self.items.get)

# cart1 = ShoppingCart("Alice", {})
# cart2 = ShoppingCart("Bob", {"Guitar": 78_800, "Fan": 7675})

# print(cart1.owner)
# print(cart2.owner)

# print(cart1.HAS_WHEELS)
# print(cart2.HAS_WHEELS)

# # Example usage:
# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)



# items = {'Laptop': 1200, 'Mouse': 25, 'Keyboard': 100, 'Monitor': 300}

# # print(max(items, key=items.get))


# # print(items.get('Mouse'))

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())

# Expected Output:
# Total cost: 1625
# Most expensive item: Laptop
# ---------------------------------------------------------------------------------------------------



# ------------------CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES-----------------

# class Square:
#     LENGTH = 4


# class Circle:

#     PI = 22 / 7


#     def __init__(self, radius: int):
#         # self.radius = radius
#         self.diameter = 2 * radius
#         self.circumference = 2 * Circle.PI * radius
#         self.square_length = Square.LENGTH


# circle_one = Circle(7)
# circle_two = Circle(3)

# print(circle_one.circumference)
# print(circle_two.diameter)

# print(Circle.PI)
# print(circle_one.PI)
# print(circle_one.square_length)

# class Circle:

#     PI = 22 / 7


#     def __init__(self, radius: int):
#         self.radius = radius
#         self.diameter = 2 * radius

#     @property
#     def circumference(self):
#         return 2 * Circle.PI * self.radius

# circle_one = Circle(7)

# print(circle_one.circumference)  # 44

# circle_one.radius = 10

# print(circle_one.circumference)

# ------------------CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES-----------------

# from datetime import datetime

# class ProgrammingLanguage:
#     def __init__(self, name, creator, is_statically_typed):
#         self.name = name
#         self.creator = creator
#         self.is_statically_typed = is_statically_typed

#     def info(self, times_to_repeat):
#         self.creation_year = 1997
#         for i in range(times_to_repeat):
#             statically_typed_language = "Yes" if self.is_statically_typed else "No"
#             print(f"{self.name} is a programming language created by {self.creator}. Is Statically typed? {statically_typed_language}. It was created in {self.creation_year}")

#     @property
#     def created_years_ago(self):
#         now = datetime.now().year
#         return now - self.creation_year



# python = ProgrammingLanguage("Python", "Guido Van Rossum", False)
# javascript = ProgrammingLanguage("JavaScript", "Brendan Eich", False)
# typescript = ProgrammingLanguage("TypeScript", "Anders Hejlsberg", True)


# python.info(2)
# javascript.info(7)
# typescript.info(2)

# languages: list[ProgrammingLanguage] = [python, javascript, typescript]

# for language in languages:
#     language.info(3)
#     print(language.created_years_ago)




# class Book:
#     def __init__(self, title: str, author: str, no_of_pages: int):
#         self.title = title
#         self.author = author
#         self.no_of_pages = no_of_pages

    
# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     def total_pages(self):
#         return sum(book.no_of_pages for book in self.books)

# book1 = Book("Things Fall Apart", "Chinua Achebe", 300)
# book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 250)

# library = Library([book1, book2])

# print(library.total_pages())  # 550 



# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def cart_item_total(self):
#         return self.price * self.quantity
    

# class Cart:
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.cart_item_total() for item in self.items)

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200

# print(dir(Library))

# paradigm - way of programming



# ---------------------------ASSIGNMENT CORRECTION-----------------------------------
# class Warehouse:
#     def __init__(self, inventory: dict[str, int]):
#         self.inventory = inventory

#     def place_order(self, order: Order):
#         for order_item in order.order_items:
#             if order_item.item_name not in self.inventory or order_item.quantity > self.inventory[order_item.item_name]:
#                 return False
            
#         for order_item in order.order_items:
#             self.inventory[order_item.item_name] -= order_item.quantity
        
#         return True
        

# class OrderItem:
#     def __init__(self, item_name, quantity):
#         self.item_name = item_name
#         self.quantity = quantity


# class Order:
#     def __init__(self, order_items: list[OrderItem]):
#         self.order_items = order_items





# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })

# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# order3 = Order([
#     OrderItem("tv", 7)
# ])

# print(warehouse.place_order(order3))


# print(warehouse.inventory)


# ---------------------------ASSIGNMENT CORRECTION-----------------------------------



# ---------------------------MAGIC DUNDER METHODS-----------------------------------
# class OrderItem:
#     def __init__(self, item_name, quantity):
#         self.item_name = item_name
#         self.quantity = quantity

#     def __str__(self):
#         return f"Order Item for {self.item_name} x{self.quantity}"  # human-readable str representation

#     def __repr__(self):
#         return f'OrderItem(item_name="{self.item_name}", quantity={self.quantity})'  # technical string representation


#     def __len__(self):
#         return self.quantity


# class Order:
#     def __init__(self, order_items: list[OrderItem]):
#         self.order_items = order_items

#     def __len__(self):
#         return len(self.order_items)

# order_item_1 = OrderItem("laptop", 9)
# order_item_2 = OrderItem("tv", 19)
# order_item_3 = OrderItem(item_name="radio", quantity=19)
# order_item_4 = OrderItem(quantity=7, item_name="blender")


# order3 = Order([
#     OrderItem("tv", 7),
#     OrderItem("tv", 7),
#     OrderItem("tv", 7),
#     OrderItem("tv", 7),
# ])

# print(len(order3))

# print(dir(order3))


# print(order_item_1)
# print(order_item_2)
# print(order_item_3)
# print(str(order_item_4))
# print(repr(order_item_4))
# print(OrderItem(item_name="blender", quantity=7).quantity)
# print(len(order_item_1))
# print(len(order_item_1))
# print(len(order_item_2))
# print(len(order_item_3))

# ---------------------------MAGIC DUNDER METHODS-----------------------------------


# -------------------------------------INHERITANCE-----------------------------------


# class Animal:
#     def __init__(self, type: str, is_wild: bool, _class: str, dentition: int | None, has_wings: bool, has_tail: bool):
#         self.type = type
#         self.is_wild = is_wild
#         self._class = _class
#         self.dentition = dentition
#         self.has_wings = has_wings
#         self.has_tail = has_tail

#     def intro(self):
#         article = "an" if self.type.startswith(("a", "e", "i", "o", "u")) else "a"
#         return f"""I am {article} {self.type}. 
# Is Wild? {self.is_wild}
# Has Wings? {self.has_wings}        
# Has Tail? {self.has_tail}
# """
    

# dog_animal = Animal("dog", False, "Mammal", 42, False, True)
# cat = Animal("cat", False, "Mammal", 56, False, True)
# eagle = Animal("eagle", True, "Aves", None, True, True)

# print(dog_animal.intro())
# print(cat.intro())
# print(eagle.intro())



# class Dog(Animal):
#     def __init__(self, breed):
#         super().__init__("dog", False, "mammal", 42, False, True)
#         self.breed = breed

#     def intro(self):
#         return f"I am a dog"
    
#     def bark(self):
#         return "I am barking"


# dog = Dog("Rottweiler")

# print(dog.intro())
# print(dog.breed)
# print(dog.bark())

# ============================================
# SIMPLE PYTHON INHERITANCE EXERCISE
# ============================================
# The student must implement two classes:
# 1. Vehicle          -> the base class
# 2. Car(Vehicle)     -> the subclass
#
# Vehicle should at least store:
#   - name

# class Vehicle:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"Vehicle: {self.name}"

# class Car(Vehicle):
#     def __init__(self, name, number_of_doors):
#         super().__init__(name)
#         self.number_of_doors = number_of_doors

#     def describe(self):
#         return f"Car: {self.name} with {self.number_of_doors} doors"


# #
# # Car should extend Vehicle and also store:
# #   - number_of_doors
# #
# # They should both have a method that returns a string description.
# #
# # Below is only usage. Students must write the classes above it.
# # ============================================

# # Create a Vehicle
# vehicle = Vehicle(name="Bicycle")
# print(vehicle.describe())
# # Expected output format (example):
# # "Vehicle: Bicycle"

# # Create a Car
# car = Car(name="Toyota", number_of_doors=4)
# print(car.describe())
# # Expected output format (example):
# # "Car: Toyota with 4 doors"


# POLYMORPHISM - Many forms

# len(), +



# class Vehicle:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"Vehicle: {self.name}"

# class Car(Vehicle):
#     def __init__(self, name, number_of_doors):
#         super().__init__(name)
#         self.number_of_doors = number_of_doors

#     def describe(self):
#         return f"Car: {self.name} with {self.number_of_doors} doors"

# bicycle = Vehicle(name="Bicycle")
# car = Car(name="Toyota", number_of_doors=4)

# vehicles = [bicycle, car]

# for vehicle in vehicles:
#     print(vehicle.describe())




# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

# class GameCharacter:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target):
#         if self == target:
#             print(f"{self.name} cannot attack themself")
#             return
        
#         print(f"{self.name} attacks {target.name}!")
#         target.health -= self.attack_power
#         print(f"{target.name}'s health is now {target.health}")



# class Warrior(GameCharacter):
#     def __init__(self, name, health, attack_power, armor):
#         super().__init__(name, health, attack_power)
#         self.armor = armor

#     def attack(self, target):
#         target.health -= 10
#         return super().attack(target)
    
# class Mage(GameCharacter):
#     def __init__(self, name, health, attack_power, mana):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana < 5:
#             print("Not enough mana to attack")
#             return
#         super().attack(target)
#         self.mana -= 5



# # 2. Create subclasses
# # Warrior
# # Has an extra attribute: armor (integer)
# # Override attack(target) so that it deals extra 10 damage.

# # Mage
# # Has an extra attribute: mana (integer)
# # Override attack(target) so that it uses 5 mana each time it attacks. 
# # If mana is less than 5, print "Not enough mana to attack".

# # 3. Handle cases where the target is the same as the attacker.
# # SAMPLE EXECUTION 1
# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# warrior.attack(mage)
# # Output:
# # Thor attacks Merlin!
# # Merlin's health is now 80
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 90
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 80
# mage.attack(warrior)
# # Output:
# # Not enough mana to attack
# print(warrior.health)  # 80
# print(mage.health)  # 80
# print(mage.mana)  # 0



# # SAMPLE EXECUTION 2
# merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
# gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 80
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 90
# gaius.attack(gaius)
# # Output:
# # Gaius cannot attack themself
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 80
# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 60
# merlin.attack(gaius)
# # Output:
# # Not enough mana to attack



# # ------------------------------------INHERITANCE-----------------------------------


# ------------------------Space Mission Correction-------------------------------


class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel

    def is_fuel_enough(self):
        if self.fuel < 50:
            print("not enough fuel to launch.")
            return False
        return True


    def launch(self):
        if self.is_fuel_enough():
            print(f"Launching {self.name}!")
            new_fuel = self.fuel - 50
            print(f"Fuel after launch: {self.fuel} - 50 = {new_fuel}")
            self.fuel = new_fuel


    def refuel(self, amount):
        if amount < 0:
            print("Cannot refuel with negative amount.")
            return
        self.fuel += amount
        print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}.")


class CargoShip(Spacecraft):
    def __init__(self, name: str, fuel: int, cargo_weight: int):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def launch(self):
        if self.is_fuel_enough():
            new_fuel = self.fuel - (50 + (self.cargo_weight * 2))
            print(f"Launching {self.name} with cargo!")
            print(f"Fuel after launch: {self.fuel} - 50 + {self.cargo_weight} * 2 = {new_fuel}")
            self.fuel = new_fuel


class PassengerShip(Spacecraft):
    def __init__(self, name: str, fuel: int, passenger_count: int):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count

    def launch(self):
        if self.passenger_count > 100:
            print("Too many passengers. Cannot launch.")
            return
        
        super().launch()


# SAMPLE EXECUTION
# Create objects
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)

# Attempt to launch both ships
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 200 - (50 + 30*2) = 90

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 100 - 50 = 50

# Refuel both ships
cargo_ship.refuel(50)
# Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

passenger_ship.refuel(30)
# Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# Launch again after refueling
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 140 - (50 + 30*2) = 30

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 80 - 50 = 30

# Try to refuel with invalid amount
cargo_ship.refuel(-10)
# Output: Cannot refuel with negative amount.

# Test PassengerShip with too many passengers
passenger_ship.passenger_count = 120
passenger_ship.launch()
# Output: Too many passengers. Cannot launch.

# Try to launch cargo ship with low fuel
cargo_ship.launch()
# Output: Not enough fuel to launch.





# ------------------------Space Mission Correction-------------------------------
