class Vehicle:
    def __init__(self,speed):
        self.speed = speed
    def move(self):
        print("Vehicle is moving")

vehicle = Vehicle(80)
vehicle.move()
print(vehicle.speed)

class Boat(Vehicle):
    def __init__(self,speed):
        self.speed = speed
    def move(self):
        print("Boat is moving")

boat = Boat(50)
boat.move()
print(boat.speed)
