from sqlite3 import connect, Connection
import os
from pandas import read_sql_query


def conn_database(path:str, name:str):
    '''
    conn_database creates a database in the user defined path and name

    Parameters
    ----------
    path : str
        path to create the database
    name : str
        name of the database file

    Returns
    -------
    con : sqlite3.Connection
        connection to the user specified database

    '''
    if not name.endswith(".db"):
        name = name+".db"
    con = connect(f"{name}")
    
    return con

def make_table(con:Connection,table_name:str,column_names:list):
    '''
    make_table creates a table in the user defined database with the table 
    name and column names defined by the user

    Parameters
    ----------
    con : Connection
        Connection to the database (assumed to be open).
    table_name : str
        Name for the table.
    column_names : list
        List of strings for the name of each column.

    Returns
    -------
    None.

    '''
    cur = con.cursor()
    
    column_name_string = ""
    for i in range(0,len(column_names)):
        if i > 0:
            column_name_string = column_name_string+","+column_names[i] 
        else:
            column_name_string=column_names[i]
    
    print(f"CREATE TABLE {table_name}({column_name_string})")
    cur.execute(f"CREATE TABLE {table_name}({column_name_string})")

def add_data_to_table(con:Connection,table_name:str,data_in:list):
    '''
    

    Parameters
    ----------
    con : Connection
        Connection to database.
    table_name : str
        Name of the table to get data from.
    data_in : list
        List of tuples of the length of the number of columns in the dataset.
        Adds the number of rows as there are columns in the dataset.

    Returns
    -------
    None.

    '''
    cur = con.cursor()
    
    # create string for each column to show what data to insert
    column_string = ""
    for i in range(0,len(data_in[0])):
        if i > 0:
            column_string = column_string+",?"
        else:
            column_string="?"
            
    # add data to table
    cur.executemany(f"""INSERT INTO {table_name} 
                    VALUES ({column_string})""",data_in)
    
    con.commit()

def read_data_from_table(con:Connection, query:str):
    '''
    

    Parameters
    ----------
    con : Connection
        Connection to database.
    query : str
        Query of the database with the form SELECT ? FROM ? WHERE ? GROUP BY ?
        .

    Returns
    -------
    data_out : TYPE
        DESCRIPTION.

    '''
    
    
    data_out = read_sql_query(query, con)
    return data_out
    



if __name__ == "__main__":
    path = os.path.curdir
    file = "tutorial.db"
    
    if os.path.isfile(path+"/"+file):
        os.remove(path+"/"+file)
    con = conn_database(path, file)
    make_table(con, "test",["title","year","score"])
    
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    add_data_to_table(con,"test",data)
    
    query = "SELECT * FROM test WHERE year > 1900 ORDER BY year DESC"
    data_out = read_data_from_table(con, query)
    
    con.close()
