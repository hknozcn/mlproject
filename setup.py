from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Read requirements from file
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # remove leading/trailing whitespaces
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) 
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Hakan',
    author_email='hknozcn8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
