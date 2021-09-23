#########################################################################################
################################_________READ.ME_________################################
#########################################################################################
#
# https://github.com/gonzalo-janer/maya-vaccine-virus-solve
#
# This script recursively finds .ma MAYA files infected with the vaccine virus.
# It outputs the absolute paths of infected files to: vaccine_infected_files.txt
#
# How to use this script:
#     1. Copy this file to the parent directory of MAYA files to scan
#     2. Open a terminal/powershell and cd into the directory with this script
#     3. Execute the script: python3 list_vaccine_infected_files.py
#     4. DONE!
#
# Terminal output will read the number and names of the infected files found.
# In this same directory, a new file can be found that lists the absolute paths.
# Name of this output file: "vaccine_infected_files.txt"
#
# Any questions or issues with this script, please contact @gonzalo-janer - github.
#
#########################################################################################
################################_______DEPENDENCIES_______###############################
#########################################################################################
#
# REQUIRES python 3.5 of higher
#
#########################################################################################

import glob
import os

# Finds files with .ma extension recursively from path of script downwards.
# RETURNS list of relative paths to .ma files.
def find_ma_files():
    ma_file_list = []
    for file_name in glob.iglob('./**/*.ma', recursive=True):
        ma_file_list.append(file_name)
    return ma_file_list

# Takes list of .ma file paths.
# Loops through list and finds files that have "vaccine" or "gene" or "breed" scriptNodes. (Signs of infection)
# RETURNS list of absolute paths to infected .ma files. 
def get_infected_files(ma_file_list):
    # trigger_word_list = ['vaccine', 'gene', 'breed', 'scriptJob']
    ma_infected_file_list = []
    for ma_file in ma_file_list:
        infected = False
        with open(ma_file, 'r') as f:
            ma_lines = f.readlines()
        for line in ma_lines:
            if line.startswith('createNode script'):
                if 'vaccine' in line or 'gene' in line or 'breed' in line:
                    infected = True
                    break
        if infected:
            abs_ma_file = os.path.abspath(ma_file) 
            ma_infected_file_list.append(abs_ma_file)
    return ma_infected_file_list

# MAIN function
def main():
    # get all .ma files
    ma_file_list = find_ma_files()
    # get infected .ma files
    ma_infected_file_list = get_infected_files(ma_file_list)
    num_infected_files = len(ma_infected_file_list)
    print()
    # print and output paths to infected files
    if num_infected_files == 0:
        print('There are 0 infected files.')
    else:
        if num_infected_files == 1:
            print('There is 1 infected file:')
        else:
            print('There are %i infected files:' % num_infected_files)
        with open('vaccine_infected_files.txt', 'w') as f:
            for infected_file in ma_infected_file_list:
                f.write(infected_file + '\n')
                print(infected_file)
        print('\nFile with paths to infected files created: vaccine_infected_files.txt\n')

if __name__ == '__main__':
    main()
