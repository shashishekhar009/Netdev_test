class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Create a car object
my_car = Car("Toyota", "Corolla", 2021)
my_car.display_info()