import os

def find_directories_with_file(directory, target_file):
    result_directories = []

    for root, dirs, files in os.walk(directory):
        if target_file in files:
            result_directories.append(root)

    return result_directories