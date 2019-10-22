from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
PROMPT = ">>> "


def main():
    current_taxi = None
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(PROMPT).lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif menu_choice == 'd':
            if current_taxi is None:
                print("You haven't chosen a taxi to drive yet!")
            else:
                bill += drive_taxi(current_taxi)
        else:
            print("Invalid Menu Choice")
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        menu_choice = input(PROMPT).lower()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    print_taxis(taxis)


def choose_taxi(taxis):
    chosen_taxi = 0
    finished = False
    print("Taxis available:")
    print_taxis(taxis)
    while not finished:
        try:
            chosen_taxi = int(input("Choose taxi: "))
            if chosen_taxi > len(taxis) - 1 or chosen_taxi < 0:
                print("That taxi doesn't exist")
            else:
                finished = True
        except ValueError:
            print("That taxi doesn't exist")
    return taxis[chosen_taxi]


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{}. {}".format(i, taxi))


def drive_taxi(taxi):
    finished = False
    while not finished:
        try:
            distance = int(input("Drive how far? "))
            if distance < 0:
                print("That's just standing still!")
            else:
                taxi.drive(distance)
                finished = True
        except ValueError:
            print("That isn't a valid distance!")
    print("Your {} trip cost ${:.2f}".format(taxi.name, taxi.get_fare()))
    return taxi.get_fare()


main()
