# maya-vaccine-solve

This is a solution to the Autodesk Maya vaccine virus. It only works for .ma files.

There's 3 files to tackle the problem and clean the files.

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

COMING SOON

## 3. delete_vaccine_remnants.py

Last step is to delete the .py files that cause new maya files to become infected.

COMING SOON
