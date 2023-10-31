# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:32:29 2023

@author: thomahm1
"""

from os import path, listdir
from platform import system

def get_data_path():
    '''
    get_data_path identifies the data path depending on if the system is
    Windows or IOS.

    Returns
    -------
    valid_system : bool
        boolean value to determine if it is an acceptable system.
    system_data_path : str
        path to install and store data.

    '''
                  
    valid_system = False
    system_data_path = str()
    if system().find("Windows") > -1:
        valid_system = True 
        system_data_path = 'C:\\Program Files (x86)\\jump_rope_database\\'
    elif system().find("Darwin") > -1:
        valid_system = True
        root_dir = path.expanduser("~")
        system_data_path = root_dir + '/Library/Application Support/jump_rope_database'
    else:
        # immediately return False and empty string
        return valid_system, system_data_path
    
    
    return valid_system, system_data_path

def find_databases(database_path:str):
    '''
    

    Parameters
    ----------
    database_path : str
        Path to the databases looking specifically for .db files

    Returns
    -------
    databases : list
        list of all database files

    '''
    
    
    
    databases=[]
    print(database_path)
    return databases