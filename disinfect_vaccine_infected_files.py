#########################################################################################
################################_________READ.ME_________################################
#########################################################################################
#
# https://github.com/gonzalo-janer/maya-vaccine-virus-solve
#
# This script disinfects .ma MAYA files infected with the vaccine virus by deleting the
# malicious "createNode script" blocks of code.
# It also creates a backup of the infected files, changing the extension from
# .ma to .ma_infected_file
#
# How to use this script:
#     1. Copy this file along with "list_vaccine_infected_files.py"
#        to a parent directory of MAYA files to scan and disinfect.
#     2. Run "list_infected_files.py" to identify infected files and generate:
#        "vaccine_infected_files.txt", needed as input to run this script.
#     3. Open a terminal/powershell and cd into the directory with this script.
#     4. Execute this script: "python3 disinfect_vaccine_infected_files.py"
#     5. DONE!
#
# You will now have .ma files disinfected from the vaccine virus + a backup copy
# of the original infected file in the same location:
#     - INITIAL STATE:   my_folder/my_file.ma                 <---infected
#     - run this script
#     - END STATE:       my_folder/my_file.ma                 <---disinfected 
#                        my_folder/my_file.ma_virus_infected  <---infected backup
#
# If you wish to delete the infected files backup, download and run:
# "delete_vaccine_infected_files_backup.py"
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

import shutil
import ntpath

# TAKES nothing
# Gets paths to infected .ma files by reading "vaccine_infected_files.txt"
# RETURNS list of paths to infected files
def get_ma_infected_files():
    try:
        with open('vaccine_infected_files.txt', 'r') as f:
            data = f.read()
    except:
        print('\nMISSING FILE: "vaccine_infected_files.txt"')
        print('Please run: "list_vaccine_infected_files.py" before running this script.')
        exit()
    ma_infected_file_list = data.split('\n')
    # skip the last one since it's an empty string caused by a \n
    return ma_infected_file_list[:-1]

# TAKES list of infected .ma files
# Cleans the .ma files by opening, reading each line and determining if it's malicious
# If the line is NOT malicious, it writes it to a new file (overwriting infected file)
# If the line is malicious, it skips it.
def disinfect_ma_files(ma_infected_file_list):
    print('DISINFECTING...')
    for ma_file in ma_infected_file_list:
        # BACKUP FILE
        backup_infected_file(ma_file)
        # READ FILE
        with open(ma_file, 'r') as f:
            ma_lines = f.readlines()
        # WRITE FILE
        virus_words = ['vaccine', '_gene', 'breed', 'leukocyte']
        with open(ma_file, 'w') as ma_clean_file:
            is_malicious_block = False
            for line in ma_lines:
                if line.startswith('createNode script'):
                    for word in virus_words:
                        if word in line:
                            is_malicious_block = True
                            break
                        else:
                            is_malicious_block = False
                    if is_malicious_block:
                        continue
                elif line[0].isspace() and is_malicious_block:
                    continue
                else:
                    is_malicious_block = False
                # WRITE LINE
                if not is_malicious_block:
                    ma_clean_file.write(line)
        ma_file_name = ntpath.basename(ma_file)
        print("DISINFECTED:", ma_file_name)
    print('\nTHE ABOVE LISTED .ma FILES HAVE BEEN BACKED UP AND DISINFECTED\n')

# TAKES string of .ma infected file path 
# Copies file to create backup of the infected file in case didinfecting corrupts it
# RETURNS nothing.
def backup_infected_file(ma_file):
    ma_file_copy = ma_file + '_virus_infected'
    try:
        shutil.copyfile(ma_file, ma_file_copy)
    except PermissionError:
        print('ERROR: Permision to copy file denied. For file:')
        print(ma_file)
    except:
        print('ERROR occured while copying file:')
        print(ma_file)

def main():
    ma_infected_file_list = get_ma_infected_files()
    disinfect_ma_files(ma_infected_file_list)

if __name__ == '__main__':
    main()
