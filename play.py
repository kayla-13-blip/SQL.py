import sqlite3
conn = sqlite3.connect("mavericks.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teams (
    TeamID INTEGER PRIMARY KEY,
    TeamName TEXT,
    City TEXT,
    Wins INTEGER,
    Losses INTEGER,
    PointsPerGame REAL
)
""")
teams = [
    (1, 'Lakers', 'Los Angeles', 50, 32, 118.5),
    (2, 'Warriors', 'Golden State', 48, 34, 120.2),
    (3, 'Celtics', 'Boston', 57, 25, 121.1),
    (4, 'Mavericks', 'Dallas', 52, 30, 117.8),
    (5, 'Bulls', 'Chicago', 40, 42, 110.4)
]
cursor.executemany("INSERT OR REPLACE INTO Teams VALUES (?, ?, ?, ?, ?, ?)", teams)
conn.commit()
print("\nAll Teams:")
for row in cursor.execute("SELECT * FROM Teams"):
    print(row)
print("\nTeams with more than 50 wins:")
for row in cursor.execute("SELECT * FROM Teams WHERE Wins > 50"):
    print(row)
print("\nTeams starting with W:")
for row in cursor.execute("SELECT * FROM Teams WHERE TeamName LIKE 'W%'"):
    print(row)
print("\nLowest Points Per Game:")
for row in cursor.execute("SELECT MIN(PointsPerGame) FROM Teams"):
    print(row)
print("\nHighest Points Per Game:")
for row in cursor.execute("SELECT MAX(PointsPerGame) FROM Teams"):
    print(row)
print("\nMavericks Team Data:")
for row in cursor.execute("SELECT * FROM Teams WHERE TeamName='Mavericks'"):
    print(row)
conn.close()