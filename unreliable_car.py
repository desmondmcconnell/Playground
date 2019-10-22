from car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = 0
        r = random.randint(100)
        if r < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
