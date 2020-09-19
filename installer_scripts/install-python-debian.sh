#!/bin/sh
# Don't Run as super user
# This file installs the appropriate version of python for this project

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
source ~/.profile

# Installing python3.8
pyenv install 3.8.5
