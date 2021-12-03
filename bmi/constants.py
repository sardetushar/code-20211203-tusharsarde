PATIENT_DATA = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

# Find total number of Overweight person
BMI_CATEGORY = 'Overweight'

BMI_HEALTH_TABLE = [
    {"BmiCategory": "Underweight", "BmiRangeKg_m2": ['below', 18.4],
     "HealthRisk": "Malnutrition risk"},
    {"BmiCategory": "Normal weight", "BmiRangeKg_m2": [18.5, 24.9],
     "HealthRisk": "Low risk"},
    {"BmiCategory": "Overweight", "BmiRangeKg_m2": [25, 29.9],
     "HealthRisk": "Enhanced risk"},
    {"BmiCategory": "Moderately obese", "BmiRangeKg_m2": [30, 34.9],
     "HealthRisk": "Medium risk"},
    {"BmiCategory": "Severely obese", "BmiRangeKg_m2": [35, 39.9],
     "HealthRisk": "High risk"},
    {"BmiCategory": "Very severely obese", "BmiRangeKg_m2": [40, 'above'],
     "HealthRisk": "Very high risk"}
]
