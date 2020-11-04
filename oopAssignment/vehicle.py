class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


ford = Vehicle(180, 22)
print("Vehicle's seed is: ", ford.max_speed, "Vehicle's mileage is: ", ford.mileage)
