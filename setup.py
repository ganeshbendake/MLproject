from setuptools import find_packages,setup
from typing import List 
hype_e_got ="-e."

def get_requirements(file_path:str)->List[str]:
    """
    this function will return a list of requirements 
    """
requirement= []

with open (file_path) as file_obj:
    requirement= file_obj.readlines()
    requirement = [req.replace("\n","") for req in requirement]

    if hype_e_got in requirement:
        requirements.remove(hype_e_got)
 
return requirement

setup(
name = 'PROJECT_1',
version = "1.1",
author ="GB",
author_email = "gbendake@gmail.com",
packages =find_packages(),
install_requires =get_requirements("requirement.txt")
)