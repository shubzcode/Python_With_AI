# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# Get the directory path (replace 'path/to/your/directory' with your actual path)
directory_path = "F:\Python full videos\My Code Practice"

# Use os.listdir() to get a list of files and directories
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
  print(item)
