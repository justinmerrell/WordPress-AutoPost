#!/bin/bash

# Navigate to the project directory
cd /opt/WordPress-AutoPost

# Create a virtual environment and activate it
python3.11 -m venv env
source env/bin/activate

# Install requirements.txt
pip install -r requirements.txt

# Make run.sh executable
chmod +x run.sh

# Add or update the cron job
(crontab -l 2>/dev/null || true; echo "0 0 * * * /opt/WordPress-AutoPost/run.sh > /opt/WordPress-AutoPost/output.log 2> /opt/WordPress-AutoPost/error.log
") | crontab -

# Deactivate the virtual environment
deactivate
