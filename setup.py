# using this file, can create this ml application as a package and even can deploy in pypi as a package

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> list[str]:
    '''
        This function will return a list of required libraries and packages
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # replace new line character with a space 
        requirements=[req.replace("\n","") for req in requirements]

        # remove -e . line when executing requirements.txt file
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Meriyan',
    author_email='it21076916@my.sliit.lk',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

