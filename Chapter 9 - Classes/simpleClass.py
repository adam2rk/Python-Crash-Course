#OOP Object oriented programming is one of the most offective ways of programming
#You write classes that represent real world things and situations and you create 
#objects based on these classes
#When you create a class you define the general behavior that a 
#whole category of objects can have

#Making an object from a class is called instantiation

class Dog:
    #simple attempt to model a dog
    
    #part of a class is the _init_() method special python ,
    # method that runs automatically when instance is made
    def __init__(self, name, age):
        #these two methods we just defined with the prefix self are avalible to every
        #method in the class
        self.name = name
        self.age = age
    #class methods
    def sit(self):
        print(f"{self.name} is now sitting")
    def rollOver(self):
        print(f"{self.name} has rolled over")

    #making an instance in the Dog Class


myDog = Dog("Willie", 4)
print(f"My Dog's name is {myDog.name} and he is {myDog.age} years old!")

    