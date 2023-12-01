from helper import validate_and_execute

user_input = ""

while user_input != "exit":
    user_input = input("Hello user, number of days and the conversion unit (hours, minutes, seconds. For example 45:hours\nType 'exit' to quit the program\n")
    if user_input != "exit":
        days_and_unit = user_input.split(":")
        days_and_unit_dict = { "days": days_and_unit[0], "unit": days_and_unit[1] }
        validate_and_execute(days_and_unit_dict)
    else:
        print("program exited... bye user :) ")