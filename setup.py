from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pypresentation',
    version='0.1.0',

    author="robertplawski",
    url="https://github.com/robertplawski/presentation-generator",

    description='Python script that generates a presentation based on a given topic',
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=find_packages(include=['pypresentation', 'pypresentation.*']),
)
