import sqlite3
conn = sqlite3.connect("basketball.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Teams")
cursor.execute("""
CREATE TABLE Teams (
    TeamID INTEGER PRIMARY KEY,
    TeamName TEXT,
    State TEXT,
    Wins INTEGER,
    PointsPerGame REAL
)
""")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (1,'Knicks','New York',50,115.2)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (2,'Nets','New York',42,110.5)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (3,'Lakers','California',48,118.3)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (4,'Warriors','California',52,120.1)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (5,'Mavericks','Texas',51,117.4)")
conn.commit()
print("Teams from New York:")
for row in cursor.execute(
    "SELECT * FROM Teams WHERE State='New York'"
):
    print(row)
print("\nNew York Team with Highest Wins:")
for row in cursor.execute("""
SELECT TeamName, Wins
FROM Teams
WHERE Wins = (
    SELECT MAX(Wins)
    FROM Teams
    WHERE State='New York'
)
"""):
    print(row)
print("\nAverage Points Per Game (New York Teams):")
for row in cursor.execute("""
SELECT AVG(PointsPerGame)
FROM Teams
WHERE State='New York'
"""):
    print(row)
conn.close()