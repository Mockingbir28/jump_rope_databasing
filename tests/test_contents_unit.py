#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 09:27:08 2023

@author: haydenthomas
"""

from jumpropedatabase.utilities import contents
from os import path
import os

folder_test = "./test"
file_name = "test.json"
data = {"database_name":"test.db",
        "database_type":"sqlite"}
data_new = {"database_name":"test_123.db",
        "database_type":"sqlite"}

# remove sql database if it exists
if os.path.isfile(folder_test+"/"+file_name):
    os.remove(folder_test+"/"+file_name)

def test_folder_creation():
    """Test creating a folder
    

    Returns
    -------
    None.

    """
    contents.make_dir(folder_test)
    assert path.exists(folder_test)


def test_json_creation():
    """create JSON file
    

    Returns
    -------
    None.

    """
    contents.make_json_file(folder_test, file_name)
    assert path.exists(path.join(folder_test, file_name))


def test_empty_json_file():
    """verify that JSON file is empty
    

    Returns
    -------
    None.

    """
    json_data = contents.read_json_data(folder_test, file_name)
    assert json_data is None

def test_add_json_data():
    '''Adds first data to JSON file
    

    Returns
    -------
    None.

    '''
    contents.update_json_data(folder_test, file_name, data)
    json_data = contents.read_json_data(folder_test, file_name)
    for key in data.keys():
        assert json_data[key] == data[key]


def test_update_json_data():
    '''Adds new data to JSON file
    

    Returns
    -------
    None.

    '''
    contents.update_json_data(folder_test, file_name, data_new)
    json_data = contents.read_json_data(folder_test, file_name)
    for key in data_new.keys():
        assert json_data[key] == data_new[key]


def test_delete_file():
    '''Prove to be able to delete file
    

    Returns
    -------
    None.

    '''
    contents.delete_file(folder_test, file_name)
    assert not path.exists(path.join(folder_test, file_name))
    

def test_remove_dir():
    ''' Test to remove directory
    

    Returns
    -------
    None.

    '''
    contents.remove_dir(folder_test)
    assert not path.exists(path.join(folder_test))