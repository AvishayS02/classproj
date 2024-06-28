from cars_package.actions import add_new_car, search


My_cars = {
    "ABC123": {
        "Year": 2020,
        "Manufacturer": "Toyota",
        "Problem": "Engine"
    },
    "XYZ456": {
        "Year": 2018,
        "Manufacturer": "Honda",
        "Problem": "10000 km treatment"
    },
    "DEF789": {
        "Year": 2022,
        "Manufacturer": "Ford",
        "Problem": "10000 km treatment+oil"
    },
    "GHI012": {
        "Year": 2019,
        "Manufacturer": "Tesla",
        "Problem": "Gear+Brakes"
    }}



def menu():
    print("Currently there are 5 cars . The current profit is: 12,000 (sum of all cars treatments)")
    while True:
        print("please choose an option:")
        print("1 - Add A Car")
        print("2 - Delete Car")
        print("3 - List of all Cars")
        print("4 - Search")
        print("5 - Exit")
        selection = input("please enter command:")
        if selection == "1":
            add_new_car()
        elif selection == "2":
            print("Delete selected")
        elif selection == "3":
            print(My_cars)
        elif selection == "4":
            search()
        elif selection == "5":
            print("exit is selected")
        