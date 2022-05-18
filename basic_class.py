class Vehicle:
    def __init__(self, maker, model,colour, price):
        self.maker = maker
        self.model=model
        self.colour=colour
        self.price=price


class Car(Vehicle):
    def __init__(self, maker, model,colour, price, seats):
        super().__init__(maker, model,colour, price)
        self.seats=seats

class Industrial_Vehicle(Vehicle):
    def __init__(self, maker, model,colour, price,lifting_wight):
        super().__init__(maker, model,colour, price)
        self.lifting_wight=lifting_wight

class Forklift(Industrial_Vehicle):
    def __init__(self, maker, model,colour, price,lifting_wight):
        super().__init__(maker, model,colour, price,lifting_wight)

class Crane(Industrial_Vehicle):
    def __init__(self, maker, model,colour, price,lifting_wight):
        super().__init__(maker, model,colour, price,lifting_wight)

car1=Car('Opel','Moca', 'black',20000,5)
forklift1=Forklift('Honda','123','jelow',58946,12)
crane1=Crane('Cato','565','red',159456,19)

print(car1.model,car1.maker,car1.colour,car1.seats,car1.price)
print(forklift1.maker,forklift1.colour,forklift1.price)
print(crane1.maker,crane1.colour,crane1.price)
