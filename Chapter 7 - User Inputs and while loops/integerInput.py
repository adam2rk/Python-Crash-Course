#The int() functions takes your value and turns it into a numerical value
#remember the input function retreives data but in the form of a string
#So if we tried using it to compare lets say to a another int value it would give as an error
#because we are trying to compare a string to a int
#so we must convert any value retreived first

age = input("Please Enter your age: ")

#at this point age is a string value and we can not do much with it
print(age)

#but if we convert we can use it in conditonals
age = int(age)

if age < 18:
    print("You pay $0")
else:
    print("You pay $50")