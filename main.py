__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

def clean_cache():
    try:
        base_path=os.getcdw()
        cache_dir=os.path.join(base_path,"files","cache")
        cache_dir = os.path.expanduser("~/Desktop/Winc project folder/files/cache")
        if os.path.exists(cache_dir):
            # If directory exists, delete contents
            for filename in os.listdir(cache_dir):
                file_path = os.path.join(cache_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
        else:
            # If directory does not exist, create it
            os.makedirs(cache_dir)
            print('Cache directory created successfully')
    except Exception as e:
        print('An error occurred: %s' % e)
def cache_zip(zip_path, cache_path):
    clean_cache()
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(cache_path)

import os

def cached_files():
    cached_files = []
    cache_path = "/path/to/cache/folder"
    # Get the absolute path to the 'files' directory
    files_dir = os.path.abspath('files')
    # Join the absolute 'files' path with the relative 'cache' path
    cache_dir = os.path.join(files_dir, 'cache')
    # Iterate through the files in the cache folder
    for the_file in os.listdir(cache_dir):
        # Add the absolute file path to the list
        file_path = os.path.join(cache_dir, the_file)
        cached_files.append(file_path)
    return cached_files
import re

def find_password(file_paths):
    password_pattern = re.compile(r'password:\s*(\S+)')
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            content = f.read()
            match = password_pattern.search(content)
            if match:
                password = match.group(1)
                return password
    return None
