from setuptools import find_packages,setup
# from typing import List

# hypen_e_dot ="-e ."
# def get_requirement(file_path:str)->List[str]:
#     requiements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]
#         if hypen_e_dot in requiements:
#             requirements.remove(hypen_e_dot)
#         return requiements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='anmol',
    author_email='anmol@70806@gmail.com',
    # install_requires=get_requirement('requirements.txt'),
    packages=find_packages()
)