from cars_package.menu import My_cars
from problems_package.problem_menu import problems_and_prices

def add_new_car():
    print("****** in add_contact")
    new_car_name = input("Please enter new car name:")
    new_car_licenseplate = input("Please enter new car number:")
    new_car_year = int(input("Please enter new car year of manifactured:"))
    new_car = {"name":new_car_name, 
                   "phone":new_car_licenseplate, 
                   "age":new_car_year}
    My_cars.append(new_car)
    print("car added succesfuly")

def search():
    print("!!!! search entered")
    search_str = input("Please enter search str:")
    found = False
    for car in My_cars:
        if (
            search_str.lower() in car["Year"].lower()  
            or search_str.lower() in car["Manufacturer"].lower()  
            or search_str.lower() in str(car["Problem"]) 
        ):
            print(f"car Year:{car["Year"]}. Manufacturer:{car["Manufacturer"]}. Problem:{car["Problem"]}")
            found = True

    if not found:
        print("not found!")
def choose_problems(car):
    car['Selected Problems'] = []  
    car['Total Cost'] = 0          #  total cost
    
    while True:
        print(f"\nSelect maintenance problems for {car['Manufacturer']} {car['Year']} {car['Problem']}:")
        print("Available Problems:")
        
        for index, (problem, price) in enumerate(problems_and_prices, start=1):
            print(f"{index}. {problem} - {price} NIS")
        
        choice = input("Choose a problem number (or 'done' to finish selecting problems): ").strip().lower()
        
        if choice == 'done':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(problems_and_prices):
            selected_problem = problems_and_prices[int(choice) - 1][0]  
            car['Selected Problems'].append(selected_problem)
            car['Total Cost'] += problems_and_prices[int(choice) - 1][1]  
            print(f"Added '{selected_problem}' to the list.")
        else:
            print("Invalid choice. Please enter a valid number or 'done'.")
    
    
    total_selected_cost = 0
    for problem in car['Selected Problems']:
        for prob, price in problems_and_prices:
            if prob == problem:
                total_selected_price += price
    
    print(f"\nTotal cost of treatments selected for {car['Manufacturer']} {car['Year']} {car['Problem']}: {total_selected_cost} NIS")
            
        

