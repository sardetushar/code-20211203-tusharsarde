import os.path
from setuptools import setup


def get_description():
    with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8", ) as file:
        return file.read()


setup(

    # library name
    name='bmi_calculator',

    # author
    author='Tushar Sarde',
    author_email='tushar.msarde@gmail.com',
    # project version
    version='0.1.0',

    description='A Python bmi calculator project',

    url='https://github.com/sardetushar/code-20211202-tusharsarde.git',

    python_requires='>=3.7',

    install_requires=[
        "pandas == 1.3.4",
        "swifter == 1.0.9",
        "coverage == 6.2",
        "pytest == 6.2.5"
    ],

    keywords='bmi calculator',

    py_modules=["bmi"],

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9'
    ]
)
