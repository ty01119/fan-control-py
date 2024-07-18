#!/bin/bash
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip

sudo apt install --upgrade python3-setuptools
sudo apt install -y python3-venv

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python -m venv venv --system-site-packages
fi

source venv/bin/activate
which python

pip install --upgrade adafruit-python-shell
sudo -E env PATH=$PATH python3 raspi-blinka.py

pip install -r ./requirements.txt
