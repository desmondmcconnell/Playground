from guitar import Guitar

guitars = []
print("My Guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    print("{} ({}) : ${:.2f} added.".format(name, year, cost))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage = " (vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {} ({}), worth $ {:.2f}{}".format(i, guitar.name, guitar.year, guitar.cost, vintage))
