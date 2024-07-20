from setuptools import find_packages,setup
from typing import List
#defining a function for the get requirements
hypen ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)

    return requirements

setup(
name = 'IPL_PREDICTION',
version='0.0.1',
author='sowmya',
author_email='sowmyapotharlanka1319@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')







)
