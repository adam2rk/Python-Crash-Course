#Positional Arguments
#When you call a function python must match each arguments with parameters
#Order matters in positional arguments

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"I have a {animal_type} and it's name is {pet_name} ")

describe_pet("Cat", "Whiskers")

#You can get unexpected results if you get the order mixed up
#keyword arguments exist for this reason to clarify the datas role in the function
#here is an example

#These next two func calls should print the same thing despite the order of the arguments
describe_pet(animal_type="Dog", pet_name="Happy")

describe_pet(pet_name="Happy", animal_type="Dog")

#Yep it worked :)