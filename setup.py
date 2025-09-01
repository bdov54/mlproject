from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirments 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requierments=file_obj.readlines()
        requierments=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='mlprject',
    version='0.0.1',
    author='Doanh',
    author_email='doanhdov@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)