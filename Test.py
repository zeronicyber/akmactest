import os
import re

def list_folders(location):
    folder_names = []
    for folder in os.listdir(location):
        if os.path.isdir(os.path.join(location, folder)):
            folder_names.append(folder)
    return folder_names

def extract_alpha_numeric(folder_names):
    alpha_numeric_names = []
    for folder_name in folder_names:
        if re.match("^[a-zA-Z0-9_]*$", folder_name):
            alpha_numeric_names.append(folder_name)
    return alpha_numeric_names

def extract_numeric_and_dot(folder_names):
    numeric_dot_names = []
    for folder_name in folder_names:
        if re.match("^[\d\.]+$", folder_name):
            numeric_dot_names.append(folder_name)
    return numeric_dot_names

location = '/path/to/folder'
folders = list_folders(location)
alpha_numeric_folders = extract_alpha_numeric(folders)
numeric_dot_folders = extract_numeric_and_dot(folders)

print("Folder names in location:")
print(folders)
print("Alpha-numeric folder names:")
print(alpha_numeric_folders)
print("Folder names containing only numbers and dots:")
print(numeric_dot_folders)
