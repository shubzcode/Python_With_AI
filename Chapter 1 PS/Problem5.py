import os
#Problem 5
#Content Path 
def list_directory_contents(path='.'):
    try:
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                print(f"{entry} (file)")
            elif os.path.isdir(full_path):
                print(f"{entry} (directory)")
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

list_directory_contents('/path/to/directory')
