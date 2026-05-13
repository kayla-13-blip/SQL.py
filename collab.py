import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
cursor = conn.cursor()
# Create Match table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Match (
id INTEGER PRIMARY KEY,
team1 TEXT,
team2 TEXT,
score1 INTEGER,
score2 INTEGER
)
""")
conn.commit()
print("Match table created")
cursor.execute("""
INSERT INTO Match (team1, team2, score1, score2)
VALUES ('India', 'Australia', 250, 245)
""")
conn.commit()
print('Opened data sucessfully')
import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)
print(tables)
matches = pd.read_sql("""SELECT * FROM Match;""", conn)
print (matches.info())
conn.close()