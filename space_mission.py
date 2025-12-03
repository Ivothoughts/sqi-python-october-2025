# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.


# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)

# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# 3. Handle negative refuel amounts.

class Spacecraft:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def launch(self):
        if self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name}!")
            print(f"Fuel after launch: {self.fuel}")
        else:
            print("Not enough fuel to launch.")

    def refuel(self, amount):
        if amount < 0:
            print("Cannot refuel with negative amount.")
        else:
            self.fuel += amount
            print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}.")


class CargoShip(Spacecraft):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def launch(self):
        fuel_needed = 50 + (self.cargo_weight * 2)
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"Launching {self.name} with cargo!")
            print(f"Fuel after launch: {self.fuel}")
        else:
            print("Not enough fuel to launch.")


class PassengerShip(Spacecraft):
    def __init__(self, name, fuel, passenger_count):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count

    def launch(self):
        if self.passenger_count > 100:
            print("Too many passengers. Cannot launch.")
        elif self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name}!")
            print(f"Fuel after launch: {self.fuel}")
        else:
            print("Not enough fuel to launch.")

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

