from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)

print(hummer)

fancy2 = SilverServiceTaxi("Fancy", 100, 2)

fancy2.drive(18)

print(fancy2.get_fare())
print(fancy2)