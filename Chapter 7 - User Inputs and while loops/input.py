#The input() function takes user input in the form of a string
#it will pause the program and wait for a user to input something into terminal
message = input("Tell me something and i will repeat it ")
print(message)

#sometimes you'll want a prompt longer than one line
#this lets you build a prompt over several lines and lets you write clean code

prompt = "If you share your name I will personalize a message more you "
prompt += "\nWhat is your first name "
firstName = input(prompt)

print(f"Hello, {firstName} it's nice to meet you have a beautiful day")
