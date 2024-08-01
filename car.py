class Car:

    def __init__(self, model, year, color, for_sale):  # attributes (variales store data)
        self.model = model
        self.year = year
        self.color = color 
        self.for_sale = for_sale


car1 = Car("BMW", 2024, "Black", False)
print(car1.year)