# author: Maddy
# date: 4/19/2026
# Purpose: present a menu to list queries 
# Changes by Kris Pepper
'''Adjusted original query from turn in due to code change and added new query to fit requirment'''

def mplayer_stats_menu(conn):
    print("\n--- Game Run Reports ---")
    print("1. Ended Game Runs With Player Score Stats (Complex) ")
    print("2. Game Runs Player Counts (LEFT JOIN)")
    print("3. Statuses Appearing More Than Once (HAVING)")
    print("4. Game Runs Longer Than Average Duration (SUBQUERY)")
    print("5. Game Runs By Current Status (GROUP BY)")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            query_score_connections(conn)
        case "2":
            query_player_count(conn)
        case "3":
            query_statuses_multiple_games(conn)
        case "4":
            query_gamerun_longer_than_avg(conn)
        case "5":
            query_gamerun_by_status(conn)
        case _:
            print("Invalid choice. Please try again.")

def query_score_connections(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT 
            g.GameID,
            g.Start,
            g.End,
            g.Won,
            g.Status,
            p.Score,
            (SELECT COUNT(*) 
             FROM Players p2 
             WHERE p2.Score = p.Score) AS PlayersWithThisScore,
            COUNT(gp.PlayerNumber) AS PlayersLinked
        FROM Gamerun g
        LEFT OUTER JOIN GamerunPlayers gp 
            ON g.GameID = gp.GameID
        LEFT OUTER JOIN Players p
            ON gp.PlayerNumber = p.PlayerNumber
        WHERE g.Status = 'Completed'
        GROUP BY 
            g.GameID, g.Start, g.End, g.Won, g.Status, p.Score
        HAVING 
            (SELECT COUNT(*) 
             FROM Players p2 
             WHERE p2.Score = p.Score) > 1
        ORDER BY p.Score;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Finished Games by Player Scores --- ")
    print("GameID | Score | PlayersWithThisScore | PlayersLinked")
    print("-" * 75)

    for row in rows:
        print(f"{row['GameID']} | {row['Score']} | "
              f"{row['PlayersWithThisScore']} | {row['PlayersLinked']}")

    cur.close()

def query_player_count(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT g.GameID,
               g.Status,
               g.Start,
               g.End,
               COUNT(gp.PlayerNumber) AS NumPlayers
        FROM Gamerun g
        LEFT OUTER JOIN GamerunPlayers gp
            ON g.GameID = gp.GameID
        GROUP BY g.GameID, g.Status, g.Start, g.End
        ORDER BY g.GameID;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Games with Player Counts (LEFT OUTER JOIN) ---")
    print("GameID | Status | Players")
    print("-" * 50)

    for row in rows:
        print(f"{row['GameID']} | {row['Status']} | {row['NumPlayers']}")

    cur.close()

def query_statuses_multiple_games(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Status,
               COUNT(*) AS NumGames
        FROM Gamerun
        GROUP BY Status
        HAVING COUNT(*) > 1
        ORDER BY NumGames DESC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Statuses Appearing More Than Once (HAVING) ---")
    print("Status | NumGames")
    print("-" * 40)

    for row in rows:
        print(f"{row['Status']} | {row['NumGames']}")

    cur.close()

def query_gamerun_longer_than_avg(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT GameID,
               Start,
               End,
               TIMESTAMPDIFF(MINUTE, Start, End) AS DurationMinutes
        FROM Gamerun
        WHERE End IS NOT NULL
          AND TIMESTAMPDIFF(MINUTE, Start, End) > (
                SELECT AVG(TIMESTAMPDIFF(MINUTE, Start, End))
                FROM Gamerun
                WHERE End IS NOT NULL
          )
        ORDER BY DurationMinutes DESC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Games Longer Than Average Duration (SUBQUERY) ---")
    print("GameID | Duration (min)")
    print("-" * 40)

    for row in rows:
        print(f"{row['GameID']} | {row['DurationMinutes']}")

    cur.close()

def query_gamerun_by_status(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Status, COUNT(*) AS NumGames
        FROM Gamerun
        GROUP BY Status
        ORDER BY NumGames DESC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Games Grouped by Status (GROUP BY) ---")
    print("Status | Number of Games")
    print("-" * 40)

    for row in rows:
        print(f"{row['Status']} | {row['NumGames']}")

    cur.close()