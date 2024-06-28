from cars_package.actions import add_new_car, search
from cars_package.menu import My_cars


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
            
if __name__ == '__main__':
    menu()
        
            
         
