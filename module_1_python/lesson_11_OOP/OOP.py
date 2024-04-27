

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.brand} {self.model} ({self.year})"

    def start_engine(self):
        return "Двигатель запущен"

    def change_year(self, year):
        self.year = year


class ElectricCar(Car):

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        return "Электродвигатель запущен"

    def get_battery_info(self):
        return f"Емкость батареи: {self.battery_capacity} кВтч"


class Truck(Car):

    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_load_info(self):
        return f"Грузоподъемность: {self.load_capacity} тонн"


car_1 = Car(brand="BMW", model="3", year=2024)
print(car_1.get_description())
print(car_1.start_engine())
car_1.change_year(2020)
print(car_1.get_description())

car_2 = ElectricCar(brand="Tesla", model="Cybertruck", year=2024, battery_capacity=85)
print(car_2.get_description())
print(car_2.start_engine())
print(car_2.get_battery_info())

car_3 = Truck(brand="Volvo", model="FM", year=2024, load_capacity=20)
print(car_3.get_description())
print(car_3.start_engine())
print(car_3.get_load_info())
