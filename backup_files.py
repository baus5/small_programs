"""Backup Program,

Simple python script for backup files and folders on MacOS

- (!!!) Dont input folder names from the terminal. Dont edit code for input from terminal.
- (Always) Assign folder names in the code editor for best result.
- (Recommended) Only use terminal input for check the folder names and before the performs.
"""

import re

# Put this script from parent folder and Run.
FOLDER_1 = "      ./[Sample Folder 1]      "
FOLDER_2 = "      ./[Sample Folder 2]      "
FOLDER_3 = "      ./[Sample Folder 3]      "
FOLDER_4 = "      ./[Sample Folder 4]      "
FOLDER_5 = "      ./[Sample Folder 5]      "
FOLDER_6 = "      ./[Sample Folder 6]      "

folders_list = [FOLDER_1, FOLDER_2, FOLDER_3, FOLDER_4, FOLDER_5, FOLDER_6]

FINAL_1 = "    ./[Sample Final Folder].     "

print()
print("These folders and files gonna be backup for final destination:")
print("Final destination:", FINAL_1)
print()

print("Folders: ")
for f in folders_list:
    clean_folder_name = re.sub(r"[^A-Za-z0-9]", "", f.strip())
    print(clean_folder_name, end=" ")
print()

# Use this For test purpose because default sample folder names include whitespaces
# clean_text = re.sub(r'[^A-Za-z0-9]', '', text)


# TODOS
# -----
# add docstring for usage
# add main function, wrap up code with functions
# simplify folder names add show folder destinations.
