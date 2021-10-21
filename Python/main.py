from car import Car
from account import Account

if __name__ == '__main__':
    car = Car("QWE234", Account("Andres Herrera", "QWE234"))
    print(vars(car))
    print(vars(car.driver))
