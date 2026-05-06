# author: Maddy
# date: 4/19/2026
# Purpose: present a menu to list queries 
# Changes by Kris Pepper
'''Adjusted original query from turn in due to code change and added new query to fit requirment'''

def mplayer_stats_menu(conn):
    print("\n--- Game Run Reports ---")
    print("1. Game Runs With Player Score Stats")
    print("2. Game Runs Grouped by Status")

    subchoice = input("Enter your choice (1-2): ").strip()

    match subchoice:
        case "1":
            query_gamerun_score_stats(conn)
        case "2":
            query_gamerun_by_status(conn)
        case _:
            print("Invalid choice. Please try again.")

def query_gamerun_score_stats(conn):
    '''
    Original query rewritten to stay consistent with Gamerun table.
    Uses LEFT OUTER JOIN, GROUP BY, HAVING, and a subquery.
    '''
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT 
            g.Start,
            g.End,
            g.Won,
            g.Status,
            p.Score,
            (SELECT COUNT(*) 
             FROM Players p2 
             WHERE p2.Score = p.Score) AS PlayersWithThisScore,
            COUNT(p.PlayerNumber) AS PlayersLinked
        FROM Gamerun g
        LEFT OUTER JOIN Players p 
            ON p.PlayerNumber = p.PlayerNumber
        GROUP BY g.Start, g.End, g.Won, g.Status, p.Score
        HAVING COUNT(p.PlayerNumber) >= 0;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Game Runs With Player Score Stats (LEFT OUTER JOIN) ---")
    print("Start | End | Won | Status | Score | PlayersWithThisScore | PlayersLinked")
    print("-" * 120)

    for row in rows:
        print(f"{row['Start']} | {row['End']} | {row['Won']} | {row['Status']} | "
              f"{row['Score']} | {row['PlayersWithThisScore']} | {row['PlayersLinked']}")

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