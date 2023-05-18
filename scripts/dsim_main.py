# dsim_main.py
# Main script for DroneSim Project
#
# Last Updated : 5/17/2023

# imports
from dsim_mainfuncs import *
from classes.dsim_configurer import Configuration

# Prompt
print("DSim tool starting...")

run_settings = init_input_loop()

print(run_settings)

print("DSim tool ending...")
