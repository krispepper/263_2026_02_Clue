# author: Deven Bernardin
# date: 4/22/2026
# Purpose: present a menu to manage the Leaderboard table
#     add/update/delete/list the table
# Changes by Kris Pepper

import mysql.connector

def leaderboard_manager_menu(conn):
    ''' This handles the menu of all the options to maintain the table '''
    while True:
        print("\n--- Maintain Leaderboard ---")
        print("1. Create (Add an Entry)")
        print("2. Delete (Remove an Entry)")
        print("3. Read (View the Leaderboard)")
        print("4. Test the Stored Procedure (Update Rank)")
        print("5. Update (Change Player Info)")

        subchoice = input("Enter choice: ").strip()

        match subchoice:
            case "1":
                add_game_run(conn)
            case "2":
                delete_game_run(conn)
            case "3":
                list_game_runs(conn)
            case "4":
                update_game_score(conn)
            case "5":
                change_game_run(conn)
            case _:
                print("Invalid choice.")

def add_game_run(conn):
    cur = conn.cursor(dictionary=True)

    print("\n=== Add Leaderboard Entry ===")
    player_number = input("Enter Player Number: ").strip()
    username = input("Enter Username: ").strip() # Fixed: Added missing input
    total_score = input("Enter Total Score: ").strip()
    games_played = input("Enter Games Played: ").strip()
    rank = input("Enter Rank: ").strip()

    query = """
        INSERT INTO Leaderboard (PlayerNumber, Username, TotalScore, GamesPlayed, `Rank`)
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cur.execute(query, (player_number, username, total_score, games_played, rank))
        conn.commit()
        print("Leaderboard entry added successfully.")
    except Exception as e:
        print("Error adding entry:", e)

    cur.close()

def change_game_run(conn):
    cur = conn.cursor(dictionary=True)

    player_number = input("Enter Player Number to update: ").strip()
    cur.execute("SELECT * FROM Leaderboard WHERE PlayerNumber = %s", (player_number,))
    row = cur.fetchone()

    if not row:
        print("Player not found on the leaderboard.")
        cur.close()
        return

    print("\nCurrent Leaderboard Entry:")
    for key, value in row.items():
        print(f"{key}: {value}")
    
    print("\nWhat would you like to update?")
    print("1. Username")
    print("2. Total Score")
    print("3. Games Played")
    print("4. Rank")

    choice = input("Select field to update: ").strip()

    field_map = {
        "1": "Username",
        "2": "TotalScore",
        "3": "GamesPlayed",
        "4": "Rank"
    }

    if choice not in field_map:
        print("Invalid choice.")
        cur.close()
        return
    
    field = field_map[choice]
    new_value = input("Enter new value: ").strip()

    query = f"UPDATE Leaderboard SET `{field}` = %s WHERE PlayerNumber = %s"

    try:
        cur.execute(query, (new_value, player_number))
        conn.commit()
        print(f"{field} updated successfully.")
    except Exception as e:
        print("Error updating entry:", e)

    cur.close()

def delete_game_run(conn, clear_all=False):
    cur = conn.cursor(dictionary=True)

    if clear_all:
        confirm = input("Clear ALL entries? (yes/no): ").strip().lower()
        if confirm == "yes":
            try:
                cur.execute("DELETE FROM Leaderboard")
                conn.commit()
                print("Leaderboard cleared.")
            except Exception as e:
                print("Error clearing leaderboard:", e)
    else:
        player_number = input("Enter Player Number to delete: ").strip()
        confirm = input("Confirm: ").strip().lower()
        if confirm != "yes":
            print("Delete cancelled.")
            cur.close()
            return
        query = "DELETE FROM Leaderboard WHERE PlayerNumber = %s"
        try:
            cur.execute(query, (player_number,))
            conn.commit()
            if cur.rowcount > 0:
                print("Entry deleted.")
            else:
                print("Player not found.")
        except Exception as e:
            print("Error deleting entry:", e)

    cur.close()

def list_game_runs(conn):
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Leaderboard ORDER BY `Rank` ASC")
    rows = cur.fetchall()

    if not rows:
        print("No entries found.")
        cur.close()
        return

    print("\nRank | PlayerNumber | Username     | Total Score | Games Played")
    print("----------------------------------------------------------------------")
    for row in rows:
        print(f"{row['Rank']}    | {row['PlayerNumber']}      | {row['Username']}  | {row['TotalScore']}        | {row['GamesPlayed']}")
    cur.close()

def update_game_score(conn):
    cur = conn.cursor(dictionary=True)
    player_number = input("Enter Player Number: ").strip()
    new_rank = input("Enter new Rank: ").strip()

    try:
        cur.callproc("UpdatePlayerRank", (player_number, new_rank))
        conn.commit()
        print("Player rank updated successfully.")
    except Exception as e:
        print("Error calling stored procedure:", e)
    cur.close()


def ensure_leaderboard_table(conn):
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Leaderboard (
            PlayerNumber INT PRIMARY KEY,
            Username VARCHAR(100),
            TotalScore INT,
            GamesPlayed INT,
            `Rank` INT
        )
        """
    )
    conn.commit()
    cur.close()


def ensure_update_rank_procedure(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            CREATE PROCEDURE IF NOT EXISTS UpdatePlayerRank(IN p_player_number INT, IN p_new_rank INT)
            BEGIN
                UPDATE Leaderboard SET `Rank` = p_new_rank WHERE PlayerNumber = p_player_number;
            END
            """
        )
        conn.commit()
    except Exception as e:
        if "already exists" not in str(e):
            print(f"Note: Stored procedure already exists or error: {e}")
    cur.close()

'''
def main():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="madelinestaley",
        password="",
        database="madelinestaley",
    )
    ensure_leaderboard_table(conn)
    ensure_update_rank_procedure(conn)
    leaderboard_manager_menu(conn)
    conn.close()


if __name__ == "__main__":
    main()
'''