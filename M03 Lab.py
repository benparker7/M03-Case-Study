class Vehicle():
    def __init__(self, type):
        self.type = type


vehicle_type = Vehicle("Car")


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


car = Automobile("", "", "", "", "")
car.type = input("What type? ")
car.year = input("What year? ")
car.make = input("What make? ")
car.model = input("What model? ")
car.doors = input("How many doors? ")
car.roof = input("What kind of roof? ")
print("--")
print("Vehicle type:", car.type)
print("Vehicle year:", car.year)
print("Vehicle make:", car.make)
print("Vehicle model:", car.model)
print("Vehicle doors:", car.doors)
print("Vehicle roof:", car.roof)
