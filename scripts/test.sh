#!/bin/bash

set -e
sudo apt install python3-venv
sudo apt install python3 -y
sudo apt install python3-pip

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 -m pytest --cov --cov-report=term-missing --cov-report xml --junitxml junit.xml