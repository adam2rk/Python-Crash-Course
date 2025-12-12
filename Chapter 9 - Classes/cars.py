class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()
    
    def fill_gass(self):
        print("Gas is being filled ")

    

myCar = Car("BMW", "M4", 2025)

print(myCar.get_descriptive_name())

#Inheritance
#Child class of Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        #super is a special function that lets you call a function from the parent class
        super().__init__(make, model, year)
        self.battry = Battery()
    
    #Overriding a method
    def fill_gass(self):
        print("This car does not have a gas tank")


#When modeling real world stuff the attributes and class can get a bit much
#So sometimes it makes sense to put them in different classes for example class 
#Battery

class Battery():
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size
        
    def get_battery_size(self):
        print(f"The battery size is {self.battery_size}")








#So this object belongs to the child class ElectricCar but the parent class 
#init has been run to set up inherited attruibutes
myLeaf = ElectricCar("Honda", "Civic", 2025)

print(myLeaf.get_descriptive_name())
myLeaf.fill_gass()
myLeaf.battry.get_battery_size()