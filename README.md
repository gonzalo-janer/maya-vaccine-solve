# Maya-Vaccine-Virus-Solve

This is a solution to the Autodesk Maya vaccine virus. It only works for .ma files.

There's 4 scripts in this repo to tackle the problem and clean the files (Currently only 3 are uploaded, tested and working). Step 4 is being developed, but can be easily taken care of manually.

## Dependencies

python3.5 or newer

## 0. INTRO

The Vaccine Virus that infects Maya files has a simple manual solution:

    1. Open the .ma files in a text editor
    2. Find the malicious blocks of code: they start with: 'createNodescript -n "vaccine_gene"; or "breed_gene", and are indented afterwards.
    3. Delete these blocks of code and save the file.
    4. Lastly, delete the .py files that the virus creates in:
        Win: <User>\Documents\maya\scripts\ or maya\<version>\scripts
        Mac: /Users/<username>/Library/Preferences/Autodesk/maya/scripts/ or maya/<version>/scripts
        
Manually cleaning a single computer and a single file is easy enough. This script automates the process and can tackle whole file structures. Ideal for scaning multiple files in a computer or server. 

4 Scripts are presented, and they do the following:

    Script 1. Find infected files
    Script 2. Disinfect the above found files and create a backup (in case anything breaks while disinfecting).
    Script 3. Delete the backups (once disinfected files are tested and confirmed to be working).
    Script 4. Delete .py files created by the virus.
    
Please read below how to use each script.

## 1. 1_list_vaccine_infected_files.py

First step is to scan the system searching for .ma files that may be infected.

### Use

     1. Copy this file to the parent directory of MAYA files to scan
     2. Open a terminal/powershell and cd into the directory with this script
     3. Execute the script: python3 1_list_vaccine_infected_files.py
     4. DONE!
Terminal output will read the number and names of infected files.

In this same directory, a new file that lists the absolute paths to infected .ma files.

Name of this output file: vaccine_infected_files.txt

## 2. 2_disinfect_vaccine_infected_files.py

Second step is to disinfect the files.

### Use

     1. Copy this file along with "list_vaccine_infected_files.py"
        to a parent directory of MAYA files to scan and disinfect.
     2. Run "list_infected_files.py" to identify infected files and generate:
        "vaccine_infected_files.txt", needed as input to run this script.
     3. Open a terminal/powershell and cd into the directory with this script.
     4. Execute this script: "python3 2_disinfect_vaccine_infected_files.py"
     5. DONE!

This script disinfects .ma MAYA files infected with the vaccine virus by deleting the malicious "createNode script" blocks of code.

It also creates a backup of the original infected files, changing the extension from .ma to .ma_infected_file, in case there's any issues with it after being disinfected. These backups can be deleted with step 3 or manually.

## 3. 3_delete_vaccine_infected_backups.py 

OPTIONAL - Delete the infected file backups created in step 2. 

This script recursively finds and deletes "vaccine" infected backups of .ma files. Said backups are created by running the 2 previous scripts of this package, resulting in .ma files being disinfected, and a backup of the infected files being created in their respective direcotries.

The extension of the backup is: .ma_virus_infected

Once you've verified that your disinfected .ma files work, you can proceed to delete the backups. This script does just that:

    - Search for files that have the ".ma_virus_infected" extension.
    - Delete those files.

### Use
     1. Copy this file to the parent directory of the infected backups to delete
     2. Open a terminal/powershell and cd into the directory with this script
     3. Execute the script: python3 3_delete_vaccine_infected_backups.py
     4. DONE!

Terminal output will read the names and number of infected backups deleted.

## 4. 4_delete_vaccine_virus_remnants.py

Last step is to delete the .py files created by the virus that cause new maya files to become infected.

COMING SOON

Meanwhile, you can manually do this step by deleting any files named: "vaccine.py", "vaccine.pyc" or "userSetup.py" in:
    
    Win: <User>\Documents\maya\scripts\ or maya\<version>\scripts
    Mac: /Users/<username>/Library/Preferences/Autodesk/maya/scripts/ or maya/<version>/scripts
