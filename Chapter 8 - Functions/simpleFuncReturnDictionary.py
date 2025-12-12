#returning a dictionary

#A function can return any kind of value including lists and dictionaries

def build_person(f_name, l_name):
    person = {"first": f_name, "last": l_name}
    return person

musician = build_person("jimi", "hendrix")

print(musician)

#passing a list into a function

def greet_users(names):
    for user in names:
        print(f"Hello, {user}")

userNames = ["Adam", "Eve"]
greet_users(userNames)