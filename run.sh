#!/bin/bash

# Activate the virtual environment
source /opt/WordPress-AutoPost/env/bin/activate

# Call the main.py script
cd /opt/WordPress-AutoPost && /opt/WordPress-AutoPost/env/bin/python main.py

# Deactivate the virtual environment
deactivate
