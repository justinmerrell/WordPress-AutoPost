#!/bin/bash
set -e

# Navigate to the project directory
cd /opt/WordPress-AutoPost

# Check if Python 3.11 is installed
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 could not be found. Please install Python 3.11 and try again."
    exit
fi

# Remove the existing virtual environment if it exists
rm -rf /opt/WordPress-AutoPost/env

# Create a virtual environment and activate it
python3.11 -m venv /opt/WordPress-AutoPost/env
source /opt/WordPress-AutoPost/env/bin/activate

# Install requirements.txt
pip install -r requirements.txt

# Make run.sh executable
chmod +x run.sh

# Add or update the cron job
# If "--live" is passed to the script, include it in the run.sh call
if [[ $* == *--live* ]]; then
    (crontab -l 2>/dev/null || true; echo "0 0 12 ? * WED * bash /opt/WordPress-AutoPost/cron/run.sh --live > /opt/WordPress-AutoPost/output.log 2> /opt/WordPress-AutoPost/error.log") | crontab -
else
    (crontab -l 2>/dev/null || true; echo "0 0 12 ? * WED * bash /opt/WordPress-AutoPost/cron/run.sh > /opt/WordPress-AutoPost/output.log 2> /opt/WordPress-AutoPost/error.log") | crontab -
fi

# Deactivate the virtual environment
deactivate
