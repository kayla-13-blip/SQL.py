"""
# Import file from your system from google.colab import files
file = files.upload()
"""
import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data sucessfully')
import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)
print(tables)