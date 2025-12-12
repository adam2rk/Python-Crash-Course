#Programming often involves examining a set of condition
#and deciding which action to take based on those conditions
#python's if statment allows you to examine the current state of
#a program and respond appropriately to the state

#The following code shows you how
#if tests lets you respond to special situtations

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    #the if catchs "bmw" and prints it in all caps the rest are handled differently
    if car == "bmw":
        print("BMW")
    else:
        print(car.title())

#case is important "BMW" and "bmw" and "Bmw" are all different values
#the double equal sign == is used to evualuate equality
#the != is used to evualuate inequality for example

requestedTopping = "mushrooms"

if requestedTopping != "anchovies":
    print("Hold the anchovies!")

#the in statment is used to check if an item is in a list

print("bmw" in cars)
#this returns true

#the if elif else chain is used when there are more than two possiblilties

#Example of more than 2 possible conditions

age = 12

if age < 4:
    print("Addmision Cost: $0")
elif age < 18:
    print("Addmision Cost: $25")
else:
    print("Addmision Cost: $40")
    