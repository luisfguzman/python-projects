import logging

logger = logging.getLogger("MAIN")

def days_to_units(num_of_days, conversion_unit):
    calculation_to_units = 0
    if conversion_unit == "hours":
        calculation_to_units = 24
    elif conversion_unit == "minutes":
        calculation_to_units = 24 * 60
    elif conversion_unit == "seconds":
        calculation_to_units = 24 * 60 * 60
    else:
        return "you entered and invalid unit, please input hours, minutes or seconds"

    return f"{num_of_days} days are {num_of_days * calculation_to_units} {conversion_unit}"       

def validate_and_execute(param_days_and_unit_dict):
    try:
        user_input_int = int(param_days_and_unit_dict["days"])
        if user_input_int > 0:
            result = days_to_units(user_input_int, param_days_and_unit_dict["unit"])
            print(result)
        elif user_input_int == 0:
            logger.error("you entered 0, please input an integer greater than 0")
        else:
            logger.error("you entered a negative value, please input an integer greater than 0")
    except ValueError:
        logger.error("you entered and invalid value, please input an integer greater than 0")