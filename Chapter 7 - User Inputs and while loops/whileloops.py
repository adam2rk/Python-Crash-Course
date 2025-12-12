#The Module operator is used to get the remainder of to items being divided
#Example the module of 4 and 3 is 1  4 % 3 == 1

#Introducing whileloops
#A while loop runs as along as certain conditions are True

currentNum = 1

while currentNum < 5:
    print(currentNum)
    currentNum += 1


#letting the user choose when to quit or exist a loop

prompt = "\nTell me something and i will repeat it "
prompt += "or you can enter quit and i will stop "

message = ""

while message != "quit":
    print(message)
    message = input(prompt)




#using a flag which is a boolean value to exist or break out of a loop

active = True

while active:
    message = input("Enter something besdies quit to continue looping ")
    if message == "quit":
        active = False
    else:
        print(message)


#using break to exist a loop


while True:
    message = input("Enter something besdies quit to continue looping ")
    if message == "quit":
        break# breaks out of loop
    else:
        print(message)

#Using continue inside a loop
#Consider a loop that counts from 1 to 10 but only prints the odd numbers
#Module will be used to determine what is odd / even and continue is used to break out of 
#the current interation if the value is even it does not need to be printed

currentNumber = 0

while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
    #It's even we continue aka leave this iteration nothing further needs to be done
        continue
    else:
        print(currentNumber)