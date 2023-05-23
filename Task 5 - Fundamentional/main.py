print(f"Yet another method for string and {50} number concatination")

calc_units = 24
name_of_unit = "hours"
# function defenition 
def days_to_units(a):
    if a > 0:
        return f"{a} days are {a * calc_units} {name_of_unit}"
    else:
        return "Invalid input! Enter positive number!"

def validate_and_exec():
    try:
        #if user_input.isdigit():
            print(days_to_units(int(num_of_days_element)))
    except ValueError:
        print("Invalid data! Exeption!")

# get input
"""
And this is multiple comment
"""
user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days! Comma Separated \n")
    for num_of_days_element in user_input.split(","):
         validate_and_exec()

