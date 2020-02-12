#!/bin/sh

# Installs pip, must be run as root
if [ "Debian" = lsb_release -i --short ]
then
  apt-get install -y python-pip
fi
