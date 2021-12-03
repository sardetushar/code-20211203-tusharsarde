## BMI v0.1.0

### Introduction

This small python project calculates body mass index for a given person details
(Height, Mass and Gender )

### Project Directory Structure

    main
        .github/
        bmi/
        tests/
        requirements.txt
        setup.py
        README.md
        LICENSE
        .coverage

### Installation

```sh
pip install -r requirements.txt
```
### Python libraries used

| Lib used | Reasons |
| ------ | ------ |
| pandas | Pandas library used for reading and processing json data. |
| swifter | To performe pandas apply on each pandas row efficiently and faster. |
| coverage | Get the code coverage report for project. |
| pytest | Testing. |
| flake8 | To adhere python coding standard. |
| bandit |  Bandit to validate and check any security and vulnaribility issues.|

## How to run ? 

Run the main.py file which will calculate the BMI for a person also final dataframe will return BmiCategory and HealthRisk.

```py
$ python main.py
````

#### Output
```
Pandas Apply: 100%|██████████| 6/6 [00:00<?, ?it/s]

| Gender | HeightCm | WeightKg  | Bmi    | BmiCategory      | HealthRisk    |
| ------ | ------   | ------    | ------ | ------           | ------        |
| Male   | 171      | 96        |   32.8 | Moderately obese |   Medium risk |
| Male   | 161      | 85        |   32.8 | Moderately obese |  Medium risk  |
| Male   | 180      | 77        |   23.8 | Normal weight    |    Low risk   |
| Female | 166      | 62        |   22.5 | Normal weight    |  Low risk     |
| Female | 150      | 70        |   31.1 | Moderately obese |  Medium risk  |
| Female | 167      | 82        |   29.4 | Overweight       | Enhanced risk |

Total number of Overweight people are: 1

Pandas Apply: 100%|██████████| 6/6 [00:00<?, ?it/s]
```

### [bmi/constants.py](https://github.com/sardetushar/code-20211202-tusharsarde/blob/main/bmi/constants.py)

Sample Patient Data - 

```json
PATIENT_DATA = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]
```

Sample BMI Table - 

```json
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
```

To Test for other type of BMI category, we just need to change **BMI_CATEGORY** variable value in constants.py file
#### Example

[BMI Category - Severly obese](https://github.com/sardetushar/code-20211202-tusharsarde/blob/c52e3690a9a80cb74a7b0b3056437385f41e68cc/tests/test_main.py#L68)

## Run tests and generate coverage report

```py
$ coverage run -m pytest && coverage report -m

================================================================================== test session starts ===================================================================================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\vamstar\bmi_calculator
collected 6 items                                                                                                                                                                         

tests\test_formulas.py .                                                                                                                                                            [ 16%]
tests\test_main.py ...                                                                                                                                                              [ 66%]
tests\test_unit_conversion.py .                                                                                                                                                     [ 83%]
tests\test_utils.py .                                                                                                                                                               [100%]

=================================================================================== 6 passed in 1.18s ====================================================================================
Name                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------
bmi\__init__.py                     0      0   100%
bmi\constants.py                    3      0   100%
bmi\formulas.py                     6      0   100%
bmi\main.py                        32      0   100%
bmi\unit_conversion.py              6      0   100%
bmi\utils.py                        7      0   100%
tests\__init__.py                   0      0   100%
tests\test_formulas.py             11      0   100%
tests\test_main.py                 40      0   100%
tests\test_unit_conversion.py      11      0   100%
tests\test_utils.py                18      0   100%
-------------------------------------------------------------
TOTAL                             134      0   100%
```

### Git Actions - Build, Test, Package and Release

    main
        .github/workflows
                publish.yml
                release.yml


#### Latest Build, Test and Package
Build and Test on [Python 3.7, 3.8, 3.9] - with coverage - Checking coding standard and finding common security issues
```html
https://github.com/sardetushar/code-20211202-tusharsarde/actions/workflows/publish.yml
```
#### Latest release
Releasing bmi app

https://github.com/sardetushar/code-20211202-tusharsarde/actions

### Reference Table - Github Actions

|Learning Source| URL |
|-------------- |---|
|Github Actions|https://github.com/actions|
|simonw - PyGotham 2021 |https://github.com/simonw/pygotham-packaging|
