__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
import shutil
import zipfile

def clean_cache():
    cache_dir = os.path.join(os.getcwd(), "cache")
    
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    
    os.makedirs(cache_dir)
    print("Cache cleaned.")

def cache_zip(zip_path, cache_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)
    
    print(f"Zip file '{zip_path}' extracted to cache directory.")

def cached_files():
    cache_dir = os.path.join(os.getcwd(), "cache")
    
    files = []
    for file_name in os.listdir(cache_dir):
        file_path = os.path.join(cache_dir, file_name)
        if os.path.isfile(file_path):
            files.append(os.path.abspath(file_path))
    
    return files

def find_password(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            if "password" in content:
                return "Password found in file: " + file_path
    
    return "Password not found in any files."

# Testing the functions
if __name__ == "__main__":
    clean_cache()
    
    zip_file_path = "data.zip"
    cache_directory = os.path.join(os.getcwd(), "cache")
    cache_zip(zip_file_path, cache_directory)
    
    files = cached_files()
    print("Cached Files:")
    for file_path in files:
        print(file_path)
    
    password = find_password(files)
    print(password)
