from bmi.formulas import calculate_bmi
from bmi.utils import get_count
import pandas as pd
import bmi.constants as const
import swifter  # noqa: F401


def get_bmi(df):
    return df.swifter.apply(
        lambda row: calculate_bmi(row.WeightKg, row.HeightCm), axis=1
    )


def bmi_cat_risk(bmi_value, bmi_table):

    bmi_category, health_risk = [], []
    for row in bmi_table.itertuples():
        try:
            if float(row.BmiRangeKg_m2[0]) <= bmi_value \
                    <= float(row.BmiRangeKg_m2[1]):
                bmi_category.append(row.BmiCategory)
                health_risk.append(row.HealthRisk)

        except ValueError:
            if 'below' == row.BmiRangeKg_m2[0]:
                if bmi_value <= float(row.BmiRangeKg_m2[1]):
                    bmi_category.append(row.BmiCategory)
                    health_risk.append(row.HealthRisk)

            if 'above' == row.BmiRangeKg_m2[1]:
                if bmi_value >= float(row.BmiRangeKg_m2[0]):
                    bmi_category.append(row.BmiCategory)
                    health_risk.append(row.HealthRisk)

    return pd.Series({'BmiCategory': "".join(bmi_category),
                      'HealthRisk': "".join(health_risk)})


def run(patient_data, bmi_category):
    bmi_df = pd.DataFrame(patient_data)
    bmi_df['Bmi'] = get_bmi(bmi_df)

    bmi_table = pd.json_normalize(const.BMI_HEALTH_TABLE)

    bmi_df[['BmiCategory', 'HealthRisk']] = bmi_df.swifter.apply(
        lambda row: bmi_cat_risk(row.Bmi, bmi_table), axis=1
    )

    # BMI table for a person
    print(bmi_df)

    # Total person
    total_person = get_count(bmi_df, 'BmiCategory', bmi_category)
    return "\nTotal number of {0} people are: {1}\n"\
        .format(bmi_category, total_person)


if __name__ == '__main__':  # pragma: no cover
    print(run(const.PATIENT_DATA, const.BMI_CATEGORY))
