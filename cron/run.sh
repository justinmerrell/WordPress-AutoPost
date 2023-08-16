#!/bin/bash
set -e

# Activate the virtual environment
source /opt/WordPress-AutoPost/env/bin/activate

# Call the main.py script with or without the --live flag
if [[ $* == *--live* ]]; then
    cd /opt/WordPress-AutoPost && /opt/WordPress-AutoPost/env/bin/python /opt/WordPress-AutoPost/main.py --live
else
    cd /opt/WordPress-AutoPost && /opt/WordPress-AutoPost/env/bin/python /opt/WordPress-AutoPost/main.py
fi

# Deactivate the virtual environment
deactivate
