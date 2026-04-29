# author: Maddy Staley 
# date: 4/25/2026
# Purpose: present a menu to manage a table 
#     add/update/delete/list the table
# Changes by Kris Pepper

def gamerun_manager_menu(conn):
    ''' This handles the menu of all the options to maintain the table
        You will be changing 'Player' to the name of your table. 
    args: 
        conn: Active MySQL database connection
    '''
    print("\n--- Game Run ---")
    print("1. Game Start")
    print("2. Game End")
    print("3. Games Won")
    print("4. Game Score")
    print("5. Dice Roll")
    print("6. Grid Fufillment")
    print("7. Current Game Run Status")

    subchoice = input("Enter your choice (1-7): ").strip()

    match subchoice:
        case "1":
            add_game_run(conn)            #
        case "2":
            delete_game_run(conn)         
        case "3":
            list_game_runs(conn)          
        case "4":
            update_game_score(conn)       
        case "5":
            change_game_run(conn)         
        case "6":
            update_game_run(conn)         
        case "7":
            update_game_run(conn)         
        case _:
            print("Invalid choice.")
           

def add_game_run(conn):
    cur = conn.cursor(dictionary=True)

    print("\n--- Start New Game Run ---")
    start = input("Enter Start datetime (YYYY-MM-DD HH:MM:SS): ").strip()
    end = input("Enter End datetime (YYYY-MM-DD HH:MM:SS): ").strip()
    won = input("Enter Won (0 or 1): ").strip()
    status = input("Enter Status: ").strip()
    score = input("Enter Score: ").strip()
    dice = input("Enter Dice Roll: ").strip()
    grid = input("Enter Official Grid: ").strip()

    query = """
        INSERT INTO GameRun (Start, End, Won, Status, Score, DiceRoll, OfficialGrid)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cur.execute(query, (start, end, won, status, score, dice, grid))
        conn.commit()
        print("Game Run started successfully.")
    except Exception as e:
        print("Error starting game run:", e)

    cur.close()


def change_game_run(conn):
    cur = conn.cursor(dictionary=True)

    start = input("Enter Start datetime of the GameRun to update: ").strip()

    cur.execute("SELECT * FROM GameRun WHERE Start = %s", (start,))
    row = cur.fetchone()

    if not row:
        print("Game Run not found.")
        cur.close()
        return

    print("\nCurrent Game Run Data:")
    for key, value in row.items():
        print(f"{key}: {value}")

    print("\nWhat would you like to update?")
    print("1. End")
    print("2. Won")
    print("3. Status")
    print("4. Score")
    print("5. DiceRoll")
    print("6. OfficialGrid")

    choice = input("Enter choice (1-6): ").strip()

    field_map = {
        "1": "End",
        "2": "Won",
        "3": "Status",
        "4": "Score",
        "5": "DiceRoll",
        "6": "OfficialGrid"
    }

    if choice not in field_map:
        print("Invalid choice.")
        cur.close()
        return

    field = field_map[choice]
    new_value = input(f"Enter new value for {field}: ").strip()

    query = f"UPDATE GameRun SET {field} = %s WHERE Start = %s"

    try:
        cur.execute(query, (new_value, start))
        conn.commit()
        print(f"{field} updated successfully.")
    except Exception as e:
        print("Error updating game run:", e)

    cur.close()


def delete_game_run(conn):
    cur = conn.cursor(dictionary=True)

    start = input("Enter Start datetime of GameRun to delete: ").strip()

    query = "DELETE FROM GameRun WHERE Start = %s"

    try:
        cur.execute(query, (start,))
        conn.commit()

        if cur.rowcount > 0:
            print("Game Run deleted.")
        else:
            print("Game Run not found.")
    except Exception as e:
        print("Error deleting game run:", e)

    cur.close()


def list_game_runs(conn):
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM GameRun")
    rows = cur.fetchall()

    if not rows:
        print("No game runs found.")
        cur.close()
        return

    print("\n--- All Game Runs ---")
    print("Start | End | Won | Status | Score | DiceRoll | OfficialGrid")
    print("-" * 80)

    for row in rows:
        print(f"{row['Start']} | {row['End']} | {row['Won']} | {row['Status']} | "
              f"{row['Score']} | {row['DiceRoll']} | {row['OfficialGrid']}")

    cur.close()


def update_game_score(conn):
    cur = conn.cursor(dictionary=True)

    start = input("Enter Start datetime of GameRun: ").strip()
    new_score = input("Enter new score: ").strip()

    try:
        cur.callproc("UpdateGameScore", (start, new_score))
        conn.commit()
        print("Game score updated successfully.")
    except Exception as e:
        print("Error calling stored procedure:", e)

    cur.close()

def update_game_run(conn):
    print("\n--- Update Game Run (General) ---")
    change_game_run(conn)