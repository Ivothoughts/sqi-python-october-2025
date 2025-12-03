# class Car:
#     def __init__(self, color, brand, model, year_manufactured, engine, no_of_doors: int):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.year_manufactured = year_manufactured
#         self.engine = engine
#         self.no_of_doors = no_of_doors


#     def move(self):
#         return f"The {self.color} {self.brand} manufactured in the year {self.year_manufactured} moved with amazing speed, thanks to the {self.engine} engine powering it"
    
#     def reverse(self):
#         return f"The {self.brand} reversed  in tight spaces without breaking a sweat."
    
#     def honk(self):
#         return f"The sound the {self.brand} makes when it honks is very annoying. I guess is a function of the {self.year_manufactured}"
    
# car1 = Car("violet", "ferari", "spider", 2021, "v12", 2)
# car2 = Car("black", "subaru", "sedan", 1999, "v6", 4)
# car3 = Car("metallic grey", "lamborghini", "urus", 2025, "v8", 4)
        
# print(car1.move())
# print(car1.reverse())
# print(car1.honk())

# print()
# print()
# print()

# print(car2.move())
# print(car2.reverse())
# print(car2.honk())

# print()
# print()
# print()

# print(car3.move())
# print(car3.reverse())
# print(car3.honk())


# class Movie:
#     def __init__(self, title: str, genre, year_released: int, no_of_cast: int, rotten_tomatoes_rating: float, is_series: bool):
#         self.title = title
#         self.genre = genre
#         self.year_released = year_released
#         self.no_of_cast = no_of_cast
#         self.rotten_tomatoes_rating = rotten_tomatoes_rating
#         self.is_series = is_series

    
#     def details(self):
#         type = "Not a series" if self.is_series else "series"
#         return f"The movie '{self.title}' has a rating of [{self.rotten_tomatoes_rating}] on rotten tomatoes, despite having ({self.no_of_cast}) stars in the cast. The movie had the highest funding for a movie released in the year {self.year_released}. I was shocked it was {self.is_series}"
        

# marvel = Movie("Far from home", "Thriller", 2022 , 10, 9.0, "series" )


# print(marvel.details())

# marvel.title = "Home-coming"

# print()
# print()

# print(marvel.details())



class CartItem:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class Cart:
    def __init__(self, carts: list[CartItem]):
        self.carts = carts

    def total(self):
        return sum(cart.price * cart.amount for cart in self.carts)

cart_item1 = CartItem("eggs", 250, 4)

cart_item2 = CartItem("bread", 1200, 6)

cart =Cart([cart_item1, cart_item2])

print(cart.total())


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
#     OrderItem("laptop", 9), 4
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

# Write the code for the example usage, just like we did today for cart and cart item.

class OrderItem:
    def __init__(self, product: str, qty: int):
        self.item_name = product
        self.qty = qty


class Order:
    def __init__(self, items: list[OrderItem]):
        self.items = items

class Warehouse:
    def __init__(self, inventory: dict[str, int]):
        self.inventory = inventory

    def place_order(self, Orders: Order) -> bool:
        for item in Orders.items:
            if item.item_name not in self.inventory or self.inventory[item.item_name] > item.qty:
                return False
            
        for item in Orders.items:
            self.inventory[item.item_name] -= item.qty
        return True




