#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:45:54 2023

@author: haydenthomas
"""

import os
from jumpropedatabase.databasing import database
from sqlite3 import Connection
from pandas import read_sql_query


# main variables
path = os.path.curdir
file = "tutorial.db"
table_name = "test"
data_input = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
query = "SELECT * FROM test WHERE year > 1900 ORDER BY year DESC"


# remove sql database if it exists
if os.path.isfile(path+"/"+file):
    os.remove(path+"/"+file)

def test_creating_database():
    '''test_creating_database tests creating a database called tutorial.db
    

    Returns
    -------
    None.

    '''
    
    con = database.conn_database(path, file)
    assert type(con) == Connection


def test_make_table():
    '''test_make_table creates a table in the database called "test" with the 
    columns title, year, and score
    

    Returns
    -------
    None.

    '''
    con = database.conn_database(path, file)
    database.make_table(con,table_name,["title","year","score"])
    data = read_sql_query("SELECT * FROM "+table_name, con)
    assert data.empty == True


def test_add_data():
    '''test_add_data adds data to the database called test
    

    Returns
    -------
    None.

    '''
    
    con = database.conn_database(path, file)
    database.add_data_to_table(con,table_name,data_input)
    data = read_sql_query("SELECT * FROM "+table_name, con)
    assert data.empty == False


def test_read_data():
    '''test_read_data tests reading in the data and verifies that the first
    entry of the year is the maximum date as defined by the query.
    

    Returns
    -------
    None.

    '''
    con = database.conn_database(path, file)
    data_out = database.read_data_from_table(con, query)
    print(data_out.year[0])
    assert data_out.year[0] == data_out.year.max()


    
    