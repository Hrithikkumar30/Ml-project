from setuptools import find_packages,setup

def get_requirements(file_path:str)->list['str']:
    '''
    this function return list of requirements
    '''
    requirements =[]
        

setup(
    name='mlprojects',
    version='0.0.1',
    author="Hrithik",
    author_email="hrithikiitian@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)