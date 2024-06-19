from car_management import CarManager
import sys



def prompt_runner():
    print("""\n------------------------------
----  WELCOME TO OUR SHOP ----
------------------------------
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
------------------------------
""")

    user_input = input("Please type number to select the option: ")
    while user_input == '':
        user_input
    validating_input(user_input)


def validating_input(num):
    try:
        int(num)
    except Exception:
        print("Only numbers are allowed")
        prompt_runner()
    else:
        num = int(num)
        if num > 0 and num < 8:
            if num == 1:
                print("\nPlease provide all of the following info\n----------------------------------------")
                make = input("Car make: ")
                model = input("Car model: ")
                year = input("Car year:")
                mileage = input("Car mileage: ")

                CarManager(make, model, year, mileage)
                print(f"\n*** Your '{make} {model} {year}' has been added to our database  ***\n\n")
                prompt_runner()

            elif num == 2:
                print(f"\nAvailable cars\n")
                cars = CarManager.all_cars
                for car in cars:
                    print(f"Car ID ({car.id}) - {(car.make).title()} {(car.model).title()}")
                prompt_runner()
            elif num == 3:
                cars = CarManager.all_cars
                print(f"\nCurrently we have a TOTAL of {len(cars)} {'car' if len(cars) == 1 else 'cars'}")
                prompt_runner()
            elif num == 4:
                querying_and_or_updating_db(num)
            elif num == 5:
                querying_and_or_updating_db(num)
            elif num == 6:
                querying_and_or_updating_db(num)
            elif num == 7:
                print("Logged out")
        else:
            print("Type a number between 1 - 7")
            prompt_runner()


def querying_and_or_updating_db(num):
    car_id = input("Please type the car ID: ")
    cars = CarManager.all_cars
    try:
        car_id = int(car_id)
    except:
        print("\nONLY numbers are allowed!")
        validating_input(4)
    else:
        for car in cars:
            if car_id == car.id:
                if num == 4:
                    print(f"\n--- {(car.make).upper()} RECORDS ---\nMake: {car.make.upper()}\nModel: {car.model.upper()}\nYear: {car.year}\nMileage: {car.mileage}\nServices: {car.services}")
                    # prompt_runner()
                elif num == 5:
                    service_update = input("\nType the service perfomed to your car: ")
                    car.services.append(service_update)
                    print(f"\nService: '{service_update}' has been added")
                    # prompt_runner()
                else:
                    current_mileage = input("\nPlease type current car's mileage: ")
                    old_mileage = car.mileage
                    car.mileage = current_mileage
                    print(f"\nYour car's old milage {old_mileage} has been updated to {current_mileage}")
                prompt_runner()
            else:
                print(f"\n{car_id} is NOT a valid ID!")
                prompt_runner()


prompt_runner()