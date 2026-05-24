import sqlite3
connection = sqlite3.connect('basketball.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    team TEXT,
    points_per_game REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY,
    team_name TEXT,
    city TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY,
    home_team TEXT,
    away_team TEXT,
    match_date TEXT
)
""")
connection.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the Basketball Database:")
for table in tables:
    print("-", table[0])
connection.close()