from bmi.unit_conversion import cm_to_meter_sq

"""
Calculate BMI using following formula
BMI(kg/m2)  = mass(kg) / height(m)2

@helper_function:-
cm_to_meter - Convert height from cm to meter square
round       - round BMI value up to 2 decimal

@Param:-
mass        - body weight in kg
height      - height in cm
"""


def calculate_bmi(weight, height):
    if weight and height:
        height_in_m2 = cm_to_meter_sq(height)
        return round(weight / height_in_m2, 1)
    else:
        return "Mass and Height should not be None or Pass valid values!"
