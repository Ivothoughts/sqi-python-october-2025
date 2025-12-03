class Vehicle:
    def __init__(self, name: str):
        self.name = name

    def describe(self):
        return f"Vehicle: {self.name}"


class Car(Vehicle):
    def __init__(self, name, number_of_doors):
        super().__init__(name)
        self.number_of_doors = number_of_doors

    def describe(self):
        return f"Car: {self.name} with {self.number_of_doors} doors"
    

vehicle = Vehicle(name="Bicycle")
print(vehicle.describe())


car = Car(name="Toyota", number_of_doors=4)
print(car.describe())
