import os
from setuptools import setup, find_packages
from setuptools.config import read_configuration
# setup_conf = read_configuration('./setup.cfg')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# directory containing the desktop applications (not the django web app)
desktop_apps_dir = 'desktop_apps/'

# package's actual folder name
calc_indicators = 'calc_indicators'
get_data = 'get_data'

# librarie's actual folder name
stt_lib = 'stt_lib'

setup(
    name='stt',
    version='0.0',
    packages=[
        calc_indicators,
        get_data,
        stt_lib
    ],
    package_dir={
        'calc_indicators': desktop_apps_dir + calc_indicators,
        'get_data': desktop_apps_dir + get_data
    },
    author="Peyton Warren",
    author_email='pwarren97@gmail.com',
    description="Stock trading tools (stt)",
    long_description=read('./README.md'),
    install_requires= [
        "iexfinance",
        "pandas",
        "pymongo"
    ],
    scripts=['desktop_apps/place-executables.sh']
)
