from taxi import Taxi

prius = Taxi("Prius1", 100)

prius.drive(40)

print(prius)
print(prius.get_fare())

prius.current_fare_distance = 0
prius.drive(100)

print(prius)
print(prius.get_fare())
