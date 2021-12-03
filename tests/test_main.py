from bmi.main import get_bmi
from bmi.main import bmi_cat_risk, run
from pandas.testing import assert_frame_equal
import bmi.constants as const
import pandas as pd


def test_get_bmi():
    data = [[169, 80], [171, 81], [172, 88]]
    df = pd.DataFrame(data, columns=['HeightCm', 'WeightKg'])
    df['Bmi'] = get_bmi(df)

    expected_data = [[169, 80, 28.0], [171, 81, 27.7], [172, 88, 29.7]]
    expected_df = pd.DataFrame(expected_data, columns=['HeightCm', 'WeightKg', 'Bmi'])
    assert assert_frame_equal(df, expected_df) is None


def test_bmi_cat_risk():
    bmi_table = pd.json_normalize(const.BMI_HEALTH_TABLE)

    # Test 1
    cat_and_risk = bmi_cat_risk(28.0, bmi_table)
    cat_and_risk_df = pd.DataFrame(cat_and_risk)

    expected = pd.Series({'BmiCategory': 'Overweight', 'HealthRisk': 'Enhanced risk'})
    expected_df = pd.DataFrame(expected)

    assert_frame_equal(expected_df, cat_and_risk_df)

    # Test 2
    cat_and_risk = bmi_cat_risk(40.2, bmi_table)
    cat_and_risk_df = pd.DataFrame(cat_and_risk)

    expected = pd.Series({'BmiCategory': 'Very severely obese', 'HealthRisk': 'Very high risk'})
    expected_df = pd.DataFrame(expected)
    assert_frame_equal(expected_df, cat_and_risk_df)

    # Test 3
    cat_and_risk = bmi_cat_risk(15.2, bmi_table)
    cat_and_risk_df = pd.DataFrame(cat_and_risk)

    expected = pd.Series({'BmiCategory': 'Underweight', 'HealthRisk': 'Malnutrition risk'})
    expected_df = pd.DataFrame(expected)
    assert_frame_equal(expected_df, cat_and_risk_df)


# final end to end test
def test_run():
    # Test1
    PATIENT_TEST1_DATA = [
        {"Gender": "Male", "HeightCm": 165, "WeightKg": 100},
        {"Gender": "Female", "HeightCm": 161, "WeightKg": 65},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 78},
    ]

    BMI_CATEGORY = 'Overweight'

    actual_1 = run(PATIENT_TEST1_DATA, BMI_CATEGORY)
    expected_1 = '\nTotal number of {0} people are: 1\n'.format(BMI_CATEGORY)
    assert actual_1 == expected_1

    # Test2
    PATIENT_TEST2_DATA = [
        {"Gender": "Male", "HeightCm": 165, "WeightKg": 100},
        {"Gender": "Female", "HeightCm": 161, "WeightKg": 99}
    ]

    BMI_CATEGORY = 'Severely obese'

    actual_2 = run(PATIENT_TEST2_DATA, BMI_CATEGORY)
    expected_2 = '\nTotal number of {0} people are: 2\n'.format(BMI_CATEGORY)
    assert actual_2 == expected_2
