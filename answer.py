import sqlite3
conn = sqlite3.connect("mavericks.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Draft (
    PlayerID INTEGER PRIMARY KEY,
    PlayerName TEXT,
    TeamName TEXT,
    Position TEXT,
    DraftYear INTEGER,
    PointsPerGame REAL
)
""")
players = [
    (1, 'John Carter', 'Lakers', 'Guard', 2022, 18.5),
    (2, 'Mike Brown', 'Warriors', 'Forward', 2021, 22.3),
    (3, 'David Lee', 'Celtics', 'Center', 2020, 15.4),
    (4, 'Chris Green', 'Mavericks', 'Guard', 2023, 19.1),
    (5, 'James White', 'Bulls', 'Forward', 2022, 11.8),
    (6, 'Kevin Hall', 'Warriors', 'Guard', 2023, 25.6)
]
cursor.executemany(
    "INSERT OR REPLACE INTO Draft VALUES (?, ?, ?, ?, ?, ?)",
    players
)
conn.commit()
print("\nDistinct Team Names:")
for row in cursor.execute(
    "SELECT DISTINCT TeamName FROM Draft"
):
    print(row)
print("\nPlayers Ordered by Points Per Game:")
for row in cursor.execute(
    "SELECT * FROM Draft ORDER BY PointsPerGame DESC"
):
    print(row)
print("\nAverage Points Per Team:")
for row in cursor.execute(
    """
    SELECT TeamName, AVG(PointsPerGame)
    FROM Draft
    GROUP BY TeamName
    """
):
    print(row)
print("\nNumber of Players in Each Position:")
for row in cursor.execute(
    """
    SELECT Position, COUNT(*)
    FROM Draft
    GROUP BY Position
    """
):
    print(row)
print("\nHighest Points Per Game:")
for row in cursor.execute(
    "SELECT MAX(PointsPerGame) FROM Draft"
):
    print(row)
print("\nLowest Points Per Game:")
for row in cursor.execute(
    "SELECT MIN(PointsPerGame) FROM Draft"
):
    print(row)
conn.close()