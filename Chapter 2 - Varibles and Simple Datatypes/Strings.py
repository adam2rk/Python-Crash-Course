'''
In some situations you'll want to use varible values inside
a string for example if you have two different varibles for the first and last name
and want to combine them. We use a f string to combine them
'''

firstName = "Adam"
lastName = "Yilmaz"

fullName = f"{firstName} {lastName}"

print(fullName)

#Adding whitespace to strings fyi print() function by default prints with a new line
print("\tPython")
print("I\nLove\nAleyna\nTilki")

#stripping whitespace in python
#.strip will take off the extra spaces before and after the hello world
print("  Hello World  ".strip())
#.lstrip() takes off left white spaces
print("  Hello World  ".lstrip())
#rstrip() takes off the right white spaces
print("  Hello World  ".rstrip())

#Removing prefixes: when working with strings another common task is to remove prefixes

userURL = "https://google.com"
print(userURL.removeprefix("https://"))