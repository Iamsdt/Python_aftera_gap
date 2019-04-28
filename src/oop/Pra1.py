# Here practice oop with car class
class Car:
    def __init__(self, name, year, cc, fuel):
        self.name = name
        self.year = year
        self.cc = cc
        self.fuel = fuel

    def get_details(self):
        details = "Name: " + self.name + "\tYear: " + str(self.year) + "\tCC:" + str(self.cc)
        print(details)

    def add_fuel(self, fuel):
        self.fuel += fuel

    def current(self):
        print("CurrentFuel: " + str(self.fuel) + "L")


class SuperCar(Car):

    def __init__(self, name, year, cc, fuel, rate):
        super().__init__(name, year, cc, fuel)
        self.rate = rate

    def run_car(self, time):
        consume = time * self.rate
        self.fuel = self.fuel - consume


if __name__ == '__main__':
    car = SuperCar("Honda", 2014, 100, 20, 0.2)
    car.get_details()
    car.current()
    car.run_car(20)
    print("After running 20 min")
    car.current()
