#*toppings argument is interesting it is called a tuple and it kinda works like a list
#but it is not mutable you can not alter it onced passed
def make_pizza(size, *toppings):
    print(f"\nMaking a pizza {size} inchs with the following toppings ")
    for topping in toppings:
        print(topping)