#!/bin/bash

# Create Virtual Env 
python3 -m venv venv
# Activate Virtual Env
source venv/bin/activate
# Update pip
pip install --upgrade pip
# Install dependencies
pip install -r requirements.txt
