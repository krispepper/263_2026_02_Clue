# author: Maddy Staley 
# date: 4/25/2026
# Purpose: present a menu to manage a table 
#     add/update/delete/list the table
# Changes by Kris Pepper

def gamerun_manager_menu(conn):
    '''
    Main menu for maintaining the Gamerun table.
    '''
    print("\n--- Game Run ---")
    print("1. Game Start")
    print("2. Game End (Delete)")
    print("3. List All Game Runs")
    print("4. Update Game Run")
    print("5. Dice Roll Update")
    print("6. Grid Fulfillment Update")
    print("7. Current Game Run Status Update")

    subchoice = input("Enter your choice (1-7): ").strip()

    match subchoice:
        case "1":
            add_game_run(conn)
        case "2":
            delete_game_run(conn)
        case "3":
            list_game_runs(conn)
        case "4":
            update_game_run(conn)
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
    gameid = input("Enter GameID: ").strip()
    start = input("Enter Start datetime (YYYY-MM-DD HH:MM:SS): ").strip()
    end = input("Enter End datetime (or leave blank): ").strip()
    won = input("Enter Won (0 or 1): ").strip()
    status = input("Enter Status: ").strip()
    dice = input("Enter Dice Roll: ").strip()
    grid = input("Enter Official Grid: ").strip()

    query = """
        INSERT INTO Gamerun (GameID, Start, End, Won, Status, DiceRoll, OfficialGrid)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cur.execute(query, (gameid, start, end if end else None, won, status, dice, grid))
        conn.commit()
        print("Game Run started successfully.")
    except Exception as e:
        print("Error starting game run:", e)

    cur.close()


def delete_game_run(conn):
    cur = conn.cursor(dictionary=True)

    start = input("Enter GameID of Gamerun to delete: ").strip()

    query = "DELETE FROM Gamerun WHERE GameID = %s"

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

    cur.execute("SELECT * FROM Gamerun")
    rows = cur.fetchall()

    if not rows:
        print("No game runs found.")
        cur.close()
        return

    print("\n--- All Game Runs ---")
    print("GameID | Start | End | Won | Status | DiceRoll | OfficialGrid")
    print("-" * 80)

    for row in rows:
        print(f"{row['GameID']} | {row['Start']} | {row['End']} | {row['Won']} | "
              f"{row['Status']} | {row['DiceRoll']} | {row['OfficialGrid']}")

    cur.close()


def update_game_run(conn):
    print("\n--- Update Game Run (General) ---")
    change_game_run(conn)


def change_game_run(conn):
    cur = conn.cursor(dictionary=True)

    start = input("Enter GameID of the Gamerun to update: ").strip()

    cur.execute("SELECT * FROM Gamerun WHERE GameID = %s", (start,))
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
    print("4. DiceRoll")
    print("5. OfficialGrid")

    choice = input("Enter choice (1-5): ").strip()

    field_map = {
        "1": "End",
        "2": "Won",
        "3": "Status",
        "4": "DiceRoll",
        "5": "OfficialGrid"
    }

    if choice not in field_map:
        print("Invalid choice.")
        cur.close()
        return

    field = field_map[choice]
    new_value = input(f"Enter new value for {field}: ").strip()

    query = f"UPDATE Gamerun SET {field} = %s WHERE GameID = %s"

    try:
        cur.execute(query, (new_value, start))
        conn.commit()
        print(f"{field} updated successfully.")
    except Exception as e:
        print("Error updating game run:", e)

    cur.close()