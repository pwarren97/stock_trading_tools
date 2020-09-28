import os
from setuptools import setup, find_packages
from setuptools.config import read_configuration
# setup_conf = read_configuration('./setup.cfg')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='stt',
    version='0.0',
    packages=find_packages(),
    author="Peyton Warren",
    author_email='pwarren97@gmail.com',
    description="Stock trading tools (stt)",
    long_description=read('./README.md'),
    install_requires= [
        "iexfinance",
        "pandas",
        'pymongo',
        'mongobox'
    ]
)
