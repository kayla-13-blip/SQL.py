import numpy as np
import pandas as pd
import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table'""",conn)
print(tables)
joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name,ci.City_Name
                          FROM country c
                          INNER JOIN city ci
                          ON c.Country_Id == ci.Country_Id""", conn)
print(joined_city)
joined_left = pd.read_sql("""SELECT*
                          FROM player
                          lEFT JOIN season
                          ON player.Player == season.Man_of_the_Series""", conn)
print(joined_left)
joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name,ci.City_Name
                           FROM country c
                           CROSS JOIN city ci""",conn)
print(joined_cross)
union = pd.read_sql("""SELECT player_Name
                    FROM player
                    UNION
                    SELECT Team Name
                    FROM team""",conn)
print(union)