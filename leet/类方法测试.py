class Car:
    def shop(self, name, price):
        print(name + "价格为：", price)


if __name__ == '__main__':
    car = Car
    car.shop(car, "宝马", 1000)
