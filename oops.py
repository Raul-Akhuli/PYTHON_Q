class Car:
    model = 'bmw'
    color = 'blue'
    def __init__(self,val1,val2):
        self.model = val1
        self.color = val2

car1 = Car('maruti 500','white')

print(Car.model)
print(Car.color)
print(car1.model)
print(car1.color)