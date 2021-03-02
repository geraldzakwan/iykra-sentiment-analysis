from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='iykra-sentiment-analysis',
    version='0.1.0',
    description='Sentiment analysis model wrapped in Flask',
    long_description=readme,
    author='Geraldi Dzakwan; IYKRA',
    author_email='geraldi.dzakwan@gmail.com',
    url='https://github.com/geraldzakwan/iykra-sentiment-analysis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
