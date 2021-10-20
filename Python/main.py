from car import Car
if __name__ == '__main__':
    car = Car()
    car.license = "CUB659"
    car.driver = "Andres Herrera"

    print(vars(car))

    car2 =  Car()
    car2.license = "QWE234"
    car2.driver = "Diego ferrer"
    print(vars(car2))