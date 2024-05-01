#!/bin/bash

echo -n "Setting up virtual invironment"
python3 -m venv .venv
source .venv/bin/activate

echo -n "Installing dependencies"
pip3 install pandas
pip3 install colored

echo -n "Complete"
python3 main.py