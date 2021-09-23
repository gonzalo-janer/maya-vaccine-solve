# maya-vaccine-virus-solve

This is a solution to the Autodesk Maya vaccine virus. It only works for .ma files.

There's 4 scripts in this repo to tackle the problem and clean the files.

## Dependencies

python3.5 or newer

## 1. list_vaccine_infected_files.py

First step is to scan the system searching for .ma files that may be infected.

### Use

     1. Copy this file to the parent directory of MAYA files to scan
     2. Open a terminal/powershell and cd into the directory with this script
     3. Execute the script: python3 list_vaccine_infected_files.py
     4. DONE!
Terminal output will read the number and names of infected files.

In this same directory, a new file that lists the absolute paths to infected .ma files.

Name of this output file: vaccine_infected_files.txt

## 2. disinfect_vaccine_infected_files.py

Second step is to disinfect the files.

### Use

     1. Copy this file along with "list_vaccine_infected_files.py"
        to a parent directory of MAYA files to scan and disinfect.
     2. Run "list_infected_files.py" to identify infected files and generate:
        "vaccine_infected_files.txt", needed as input to run this script.
     3. Open a terminal/powershell and cd into the directory with this script.
     4. Execute this script: "python3 disinfect_vaccine_infected_files.py"
     5. DONE!

This script disinfects .ma MAYA files infected with the vaccine virus by deleting the malicious "createNode script" blocks of code.

It also creates a backup of the original infected files, changing the extension from .ma to .ma_infected_file, in case there's any issues with it after being disinfected. These backups can be deleted with step 3 or manually.

## 3. delete_vaccine_infected_backups.py 

OPTIONAL - Delete the infected file backups created in step 2. 

COMING SOON

## 4. delete_vaccine_remnants.py

Last step is to delete the .py files that cause new maya files to become infected.

COMING SOON
