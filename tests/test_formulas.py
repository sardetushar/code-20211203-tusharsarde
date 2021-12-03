from bmi.formulas import calculate_bmi


def test_calculate_bmi():
    # valid parameters
    mass = 80  # in Kg
    height = 172  # in cm
    bmi = calculate_bmi(mass, height)
    expected = 27.0
    assert bmi == expected

    # invalid parameters
    mass = None
    bmi = calculate_bmi(mass, height)
    expected_err_msg = "Mass and Height should not be None or Pass valid values!"
    assert bmi == expected_err_msg
