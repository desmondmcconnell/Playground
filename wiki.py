import wikipedia


page = input("Which page would you like a summary of? ")
while not page == "":
    try:
        print(wikipedia.summary(page))
    except wikipedia.exceptions.DisambiguationError as error:
        print("The following options are available. Please select one by entering the corresponding number")
        for i, option in enumerate(error.options, 1):
            print("{}. {}".format(i, option))
        valid_number_chosen = False
        while not valid_number_chosen:
            try:
                number = int(input("Please enter a number: "))
                if number < 1 or number > len(error.options):
                    print("You must enter a valid number from the list shown")
                else:
                    page = error.options[number - 1]
                    valid_number_chosen = True
            except ValueError:
                print("You must enter a valid number from the list shown")

        print(wikipedia.summary(page))
    except wikipedia.exceptions.PageError:
        print("That page does not exist")
    page = input("\nWhich page would you like a summary of? ")
