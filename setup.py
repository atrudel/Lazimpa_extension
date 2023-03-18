from setuptools import setup, find_packages


with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name='Lazimpa_extension',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/atrudel/Lazimpa_extension',
    license='',
    author='',
    author_email='',
    description='Extension of the LazImpa repository by MathieuRita',
    python_requires='>=3.7',
    install_requirements=requirements
)
