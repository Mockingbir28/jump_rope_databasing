# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 07:41:52 2023

@author: thomahm1
"""

from os import path, mkdir, rmdir, remove
import json

def make_dir(path_name:str):
    '''Creates a directory assuming it does not already exist.
    

    Parameters
    ----------
    path_name : str
        Path to create the folder for storing data. For example database 
        folders, executable folder, etc.

    Returns
    -------
    None.

    '''
    if not path.exists(path_name):
        mkdir(path_name)
        print("Created " + path_name)
    else:
        print(path_name + ' already exists')
    
def make_json_file(path_name:str, json_name:str):
    '''Creates a JSON file in the user defined path
    

    Parameters
    ----------
    path_name : str
        Path to create the JSON file.
    json_name : str
        Name of the JSON file.

    Returns
    -------
    None.

    '''
    
    file_name = path.join(path_name, json_name)
    if not path.isfile(file_name):
        open(file_name, "w+")
        print("Created " + file_name)
    else:
        print(file_name + ' already exists')

def add_json_data(path_name:str, json_name:str, new_json_data:dict):
    
    file_name = path.join(path_name, json_name)
    json_file_data = json.loads(file_name)
    
    

if __name__ == "__main__":
    # test creating a folder
    folder_test = "./test"
    make_dir(folder_test)
    
    # test an already created folder
    make_dir(folder_test) # should only generate a 
    
    # test creating a JSON file
    file_name = "test.json"
    make_json_file(folder_test, file_name)
    
    # test trying to create an existing JSON file
    make_json_file(folder_test, file_name)
    
    remove(path.join(folder_test, file_name))
    rmdir(folder_test)