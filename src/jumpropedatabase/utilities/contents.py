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

def update_json_data(path_name:str, json_name:str, new_json_data:dict):
    '''update_json_data adds distionary data in new_json_data into the user 
    defined JSON file.
    

    Parameters
    ----------
    path_name : str
        Path to the JSON file.
    json_name : str
        JSON file name.
    new_json_data : dict
        Dictionary with new JSON data. If there is overlap with the data in 
        the JSON file, then it will replace/update the data

    Returns
    -------
    None.

    '''
    
    # read JSON file
    file_name = path.join(path_name, json_name)
    json_file = open(file_name,"r");
    json_str = json_file.read()
    json_file.close()
    
    # update JSON data
    if len(json_str) > 0:
        json_file_data = json.loads(json_str)
        
        # compare keys
        json_file_data.update(new_json_data)
    else:
        # add new data
        json_file_data = new_json_data
    
    # update json file
    json_new = json.dumps(json_file_data)
    json_file = open(file_name, "w")
    json_file.write(json_new)


def read_json_data(path_name:str, json_name:str):
    '''
    

    Parameters
    ----------
    path_name : str
        Directory of file.
    json_name : str
        JSON file name.

    Returns
    -------
    json_data : dict
        json data contents as a dictionary.

    '''
    
    file_name = path.join(path_name, json_name)
    json_file = open(file_name,"r");
    json_str = json_file.read()
    json_file.close()
    
    # update JSON data
    if len(json_str) > 0:
        json_data = json.loads(json_str)
    
    else:
        json_data = None
    
    return json_data
    

def delete_file(path_name:str, file_name:str):
    '''Deletes the user defined file
    

    Parameters
    ----------
    path_name : str
        path to file.
    file_name : str
        file name to delete.

    Returns
    -------
    None.

    '''
    file = path.join(path_name, file_name)
    if path.exists(file):
        remove(file)
    

def remove_dir(path_name:str):
    '''Deletes the user defined folder
    

    Parameters
    ----------
    path_name : str
        folder to be deleted

    Returns
    -------
    None.

    '''
    if path.exists(path_name):
        rmdir(path_name)
    

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
    
    # add data to JSON file
    data = {"database_name":"test.db",
            "database_type":"sqlite"}
    update_json_data(folder_test, file_name, data)
    
    # test updating JSON file
    data = {"database_name":"test_123.db",
            "database_type":"sqlite"}
    update_json_data(folder_test, file_name, data)
    
    delete_file(folder_test, file_name)
    remove_dir(folder_test)