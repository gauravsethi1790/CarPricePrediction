from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:

    requirements=[]
    with open(filepath) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(

    name="Car Price Prediction",
    version="1.0.0",
    author="Gaurav Sethi",
    author_email="gauravsethi1790@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)