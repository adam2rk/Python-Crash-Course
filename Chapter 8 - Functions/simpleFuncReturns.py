#Return values
#A function doesn't always have to display
#its output it can process data and return it
#called a return value

#This following function will take the first and last name
#and return the full name in a formatted maner

def get_formatted_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()

print(get_formatted_name("jimi", "hendrix"))