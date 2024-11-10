"""class Car:  # 

    num_cars = 0       # class variable

    def __init__(self, model, year, color, for_sale):  # attributes (variales store data)
        self.model = model  
        self.year = year     
        self.color = color   # instances variables
        self.for_sale = for_sale
        Car.num_cars +=1


    def drive(self):
        print(f'you drive a {self.color} {self.model} ')
        print(f'there is {Car.num_cars}  car(s) in total')"""




# ------------------Inheritance allow class inherate attribute and methods from another class------------------------------


"""class Animals:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animals):

    pass

class Cat(Animals):

    pass

dog = Dog('scooby') 
cat = Cat('catty')
print(dog.name, dog.is_alive, dog.sleep())"""


# ---------   mutli inheritance -------

"""class prey:

    def flee(self):
        print('this animal is fleeng')

class predator:
    def hunt(self):
        print('this animal is hungting')

class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class fish (prey, predator):
    pass

rabbit =  Rabbit()
#print(rabbit.flee())

hawk = Hawk()
#print(hawk.hunt())

fishs = fish()

print(fishs.flee(), fishs.hunt())"""

"""class Car:
    num_car = 0 
    def __init__(self, model, year, color):
        self.model = model
        self.year = year 
        self.color = color
        Car.num_car += 1 

    def drive(self):
        print(f'You drive {self.model} {self.color} {self.year} {Car.num_car}')
        print(f'You drive {self.model} {self.color} {self.year} {Car.num_car}')


car = Car('BMW', 2024, 'black')
car.drive()"""

