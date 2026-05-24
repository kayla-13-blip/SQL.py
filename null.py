import sqlite3
conn = sqlite3.connect("mavericks.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teams (
    TeamID INTEGER PRIMARY KEY,
    TeamName TEXT NOT NULL,
    City TEXT NOT NULL,
    Wins INTEGER CHECK(Wins >= 0),
    Losses INTEGER CHECK(Losses >= 0),
    PointsPerGame REAL
)
""")
teams = [
    (1, 'Lakers', 'Los Angeles', 50, 32, 118.5),
    (2, 'Warriors', 'Golden State', 48, 34, 120.2),
    (3, 'Celtics', 'Boston', 57, 25, None),
    (4, 'Mavericks', 'Dallas', 52, 30, 117.8),
    (5, 'Bulls', 'Chicago', None, 42, 110.4)
]
cursor.executemany(
    "INSERT OR REPLACE INTO Teams VALUES (?, ?, ?, ?, ?, ?)",
    teams
)
conn.commit()
print("\nAll Team Data:")
for row in cursor.execute("SELECT * FROM Teams"):
    print(row)
print("\nTeams with NULL PointsPerGame:")
for row in cursor.execute(
    "SELECT * FROM Teams WHERE PointsPerGame IS NULL"
):
    print(row)
print("\nTeams with NULL Wins:")
for row in cursor.execute(
    "SELECT * FROM Teams WHERE Wins IS NULL"
):
    print(row)
print("\nTeams with Available PointsPerGame:")
for row in cursor.execute(
    "SELECT * FROM Teams WHERE PointsPerGame IS NOT NULL"
):
    print(row)
print("\nAverage Points Per Game:")
for row in cursor.execute(
    "SELECT AVG(PointsPerGame) FROM Teams"
):
    print(row)
conn.close()