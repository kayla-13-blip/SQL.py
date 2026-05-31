import sqlite3

conn = sqlite3.connect("basketball.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Players")
cursor.execute("DROP TABLE IF EXISTS Teams")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teams (
    TeamID INTEGER PRIMARY KEY,
    TeamName TEXT,
    City TEXT,
    Wins INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Players (
    PlayerID INTEGER PRIMARY KEY,
    PlayerName TEXT,
    TeamID INTEGER,
    Position TEXT,
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
)
""")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (1,'Lakers','Los Angeles',50)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (2,'Warriors','Golden State',48)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (3,'Celtics','Boston',57)")
cursor.execute("INSERT OR REPLACE INTO Teams VALUES (4,'Mavericks','Dallas',52)")
cursor.execute("INSERT OR REPLACE INTO Players VALUES (101,'John Carter',1,'Guard')")
cursor.execute("INSERT OR REPLACE INTO Players VALUES (102,'Mike Brown',2,'Forward')")
cursor.execute("INSERT OR REPLACE INTO Players VALUES (103,'David Lee',3,'Center')")
cursor.execute("INSERT OR REPLACE INTO Players VALUES (104,'Chris Green',4,'Guard')")
conn.commit()
print("\nINNER JOIN")
for row in cursor.execute("""
SELECT Players.PlayerName, Teams.TeamName
FROM Players
INNER JOIN Teams
ON Players.TeamID = Teams.TeamID
"""):
    print(row)
print("\nLEFT JOIN")
for row in cursor.execute("""
SELECT Teams.TeamName, Players.PlayerName
FROM Teams
LEFT JOIN Players
ON Teams.TeamID = Players.TeamID
"""):
    print(row)
print("\nUNION")
for row in cursor.execute("""
SELECT TeamName AS Name FROM Teams
UNION
SELECT PlayerName FROM Players
"""):
    print(row)
conn.close()