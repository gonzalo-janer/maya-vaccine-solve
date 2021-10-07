#########################################################################################
################################_________READ.ME_________################################
#########################################################################################
#
# https://github.com/gonzalo-janer/maya-vaccine-virus-solve
#
# This script recursively finds and deletes "vaccine" infected backups of .ma files.
# Said backups are created by running the 2 previous scripts of this package,
# resulting in .ma files being disinfected, and a backup of the infected files 
# being created in their respective direcotries.
#
# The extension of the backup is: .ma_virus_infected
#
# Once you've verified that your disinfected .ma files work, you can proceed to delete
# the backups. This script does just that:
#     - Search for files that have the ".ma_virus_infected" extension.
#     - Delete those files.
#
# How to use this script:
#     1. Copy this file to the parent directory of the infected backups to delete
#     2. Open a terminal/powershell and cd into the directory with this script
#     3. Execute the script: python3 delete_vaccine_infected_backups.py
#     4. DONE!
#
# Terminal output will read the names and number of infected backups deleted.
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

# Finds files with ".ma_virus_infected" extension recursively from path of script downwards.
# RETURNS list of relative paths to infected backup files.
def find_bak_files():
    bak_file_list = []
    for file_name in glob.iglob('./**/*.ma_virus_infected', recursive=True):
        bak_file_list.append(file_name)
    return bak_file_list

# TAKES list of backup files to delete
# Deletes files
# RETURNS nothing
def delete_files(bak_file_list):
    # If list isn't empty - delete files in list
    if bak_file_list:
        counter = 0
        for bak in bak_file_list:
            try:
                os.remove(bak)
                print('DELETED:', bak)
                counter += 1
            except:
                print('ERROR, could not delete:', bak)
        print()
        print('TOTAL INFECTED FILES DELETED:', counter)
        print()
    else:
        print('THERE ARE NO INFECTED BACKUP FILES TO DELETE')

# MAIN function
def main():
    # get all infected bakup files
    bak_file_list = find_bak_files()
    # Delete infected backup files
    delete_files(bak_file_list)

if __name__ == '__main__':
    main()
