import os
from Check_if_py import is_python_file
import re
# Set the directory path and the prefix
directory = os.getcwd()
prefix = input('What would you like to change the prefix to?:\n')

# Get a list of all the files in the directory
filenames = os.listdir(directory)

# Iterate through the filenames and rename each file

for filename in filenames:
    # Checks if files in Current Directory are Python Files
    py_file = is_python_file(filename=filename)
    if py_file == False:
        # Loops through all files in Directory and renames all non-python files
        old_name = os.path.join(directory, filename)
        new_name = os.path.join(directory, prefix + filename)
        os.rename(old_name, new_name)
    else:
        pass
print('Renaming complete!')
