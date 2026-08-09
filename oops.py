class Car:
    model = 'bmw'
    color = 'blue'
    def __init__(self,val1,val2,val3):
        self.model = val1
        self.color = val2
        self.price = val3

car1 = Car('maruti 500','white', 500000)

print(Car.model)
print(Car.color)
print(car1.model)
print(car1.color)
print(car1.price)