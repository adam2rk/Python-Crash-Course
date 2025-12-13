from name_func import get_formatted_name

print("Please Enter q if you want to quit")
while True:
    first = input("Please enter your first name: ")
    if first == "q":
        break
    last = input("Please enter your last name: ")
    if last == "q":
        break

    formattedName = get_formatted_name(first, last)
    print(formattedName)

    #we can see the program runs correctly but we want to modify it so that we can
    #middle names aswell as we do so we want to make sure we dont break the function
    