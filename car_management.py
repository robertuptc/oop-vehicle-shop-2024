class CarManager:
    all_cars = []
    cars_counter = 1

    def __init__(self, make, model, year, mileage):
        self.id = CarManager.cars_counter
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = []
        
        CarManager.all_cars.append(self)
        CarManager.cars_counter += 1