#!/bin/bash

# Activate the virtual environment
source /root/automation/WordPress-AutoPost/env/bin/activate

# Call the main.py script
python /root/automation/WordPress-AutoPost/main.py

# Deactivate the virtual environment
deactivate
