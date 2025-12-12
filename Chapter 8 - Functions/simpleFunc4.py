#Default values 
#A Default value exists in a function parameter if you don't pass an argument it will
#use the default value
#Example of this
#So if the func call fails to pass a animal type the func will assume it's a dog
def describe_pet(pet_name, animal_type = "Dog"):
    print(f"I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")

describe_pet("Happy")
describe_pet("Happy", "Cat")