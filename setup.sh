#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python -m venv venv
fi

source ~/projects/fan-control-py/venv/bin/activate
which python

pip install -r requirements.txt