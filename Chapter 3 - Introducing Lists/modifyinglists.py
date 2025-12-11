motorcycles = ["Honda", "Yamaha", "Suzuki"]

#the following code will modify the list by changing the first element "Honda" to "Ducati"

motorcycles[0] = "Ducati"

#adding an element to a list
#appending a element at the end of a list which is the simplest way

motorcycles.append("Honda")

print(motorcycles)

#removing an element using the del statement
#this statment is used if you know the index of the element you want to remove
zipCodes = [10735, 33256, 10482]
del zipCodes[0]
print(zipCodes)

#removing an item inside a list
#if you know the location del statment is used

del zipCodes[0]

#removing an item using the pop method lets you use it afterwards
#pop removes the last item in the list unless specified you could also put the
#index of the element inside the pop method
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)