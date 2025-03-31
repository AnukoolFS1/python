#creating a class

class Car:
    def __init__(self, brand, model): #constructor initializer
        self.brand = brand
        self.model = model
    
    def show_details(self): #instance method
        print(f"Car: {self.brand} {self.model}")
    

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# print(car1.show_details(), "weqr")
# print(car2.show_details(), "weqr")