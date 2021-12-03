from bmi.utils import get_square

"""
Unit Conversion

@functions:-
cm_to_meter

@helper_functions:-
get_square
"""


# convert cm to meter square
def cm_to_meter_sq(val_in_cm):
    try:
        return get_square(val_in_cm / 100.0)
    except TypeError:
        raise "Invalid centimeter value and can not convert to meter square"
