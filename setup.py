from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_reqs(path:str) -> List[str]:
    requirements = []
    with open(path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name = 'ML_Project',
    version = '0.0.0',
    author = 'Yash Paddalwar',
    author_email = 'yash9096.p@gmail.com',
    packages = find_packages(),
    install_requires = get_reqs('requirements.txt')
)