#Python uses special objects called exceptions to handle errors

#Handling a zero division error

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero dummy")