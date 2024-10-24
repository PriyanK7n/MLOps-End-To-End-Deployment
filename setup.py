from setuptools import find_packages, setup
from typing import List

# for ignoring purposes when running requirements.txt 
HYPEN_E_DOT='-e .' # for ignoring purposes when running requirements.txt 

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # returns a list but also contains \n character in every element
        requirements = [ req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='MLOPS-PROJECT',
version='0.0.1',
author='Priyank',
author_email='peiyank99@gmail.com',

packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)
