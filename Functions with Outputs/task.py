#format name function
def format_name(f_name, l_name):
    return f"{l_name.title()}, {f_name.title()}"

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

#this line calls function, then returns the f string above, then prints it
print(format_name(first_name, last_name))

