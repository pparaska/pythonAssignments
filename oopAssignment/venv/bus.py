class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

volvo_bus = Bus('School Volvo', 180, 12)
print('Vehicle Name:', volvo_bus.name, 'Speed:', volvo_bus.max_speed, 'Mileage:', volvo_bus.mileage)