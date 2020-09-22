#!/bin/sh
# This file is for installing python with the appropriate version via pyenv
# Must run platform specific setup script first

# Install dependencies and pip3 for debian
INSTALLONDEBIAN=./install-debian-dependencies.sh
chmod +x $INSTALLONDEBIAN
/bin/sh $INSTALLONDEBIAN

# Install pyenv and python 3.8.5
curl https://pyenv.run | sh
pyenv install 3.8.5

cd ../
pyenv local 3.8.5
cd ./installer_scripts

# Install python libraries with pip
pip3 install -r ../requirements.txt
