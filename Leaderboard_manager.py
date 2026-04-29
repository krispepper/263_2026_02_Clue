# author: Deven Bernardin
# date: 4/22/2026
# Purpose: present a menu to manage the Leaderboard table
#     add/update/delete/list the table
# Changes by Kris Pepper


def leaderboard_manager_menu(conn):
    print("\n--- Maintain Leaderboard ---")
    print("1. Add Leaderboard Entry")
    print("2. Change Leaderboard Entry")
    print("3. Delete Leaderboard Entry")
    print("4. List Leaderboard")
    print("5. Update Leaderboard Score (Stored Procedure)")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            add_leaderboard(conn)
        case "2":
            change_leaderboard(conn)
        case "3":
            delete_leaderboard(conn)
        case "4":
            list_leaderboard(conn)
        case "5":
            update_leaderboard_score(conn)
        case _:
            print("Invalid choice. Please try again.")


def add_leaderboard(conn):
    """Add a new leaderboard entry.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Add Leaderboard Entry ---")

    player_id = input("Enter Player ID: ")
    score = input("Enter Score: ")

    # ✅ YOUR ORIGINAL QUERY
    cur.execute(
        "INSERT INTO Leaderboard (PlayerID, Score) VALUES (%s, %s)",
        (player_id, score),
    )

    conn.commit()
    print('rows inserted: ', cur.rowcount)

    if cur.rowcount == 1:
        print(f"Leaderboard entry for Player {player_id} added successfully!")
    else:
        print('An error occurred adding the leaderboard entry')

    cur.close()


def change_leaderboard(conn):
    """Update leaderboard information in the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Change Leaderboard Entry ---")

    player_id = input("Enter Player ID to change: ")

    cur.execute("SELECT * FROM Leaderboard WHERE PlayerID = %s", (player_id,))
    record = cur.fetchone()

    if not record:
        print("Record not found!")
        cur.close()
        return

    print(f"Current leaderboard data: {record}")

    print("\nWhich field would you like to change?")
    print("1. Score")

    field_choice = input("Enter your choice: ")

    field_map = {
        "1": "Score",
    }

    if field_choice not in field_map:
        print("Invalid choice!")
        cur.close()
        return

    field_name = field_map[field_choice]
    new_value = input(f"Enter new {field_name} (current: {record[field_name]}): ")

    cur.execute(
        f"UPDATE Leaderboard SET {field_name} = %s WHERE PlayerID = %s",
        (new_value, player_id),
    )

    conn.commit()
    print('rows updated: ', cur.rowcount)

    if cur.rowcount == 1:
        print(f"Leaderboard {field_name} updated successfully!")
    else:
        print('An error occurred updating the leaderboard')

    cur.close()


def delete_leaderboard(conn):
    """Delete a leaderboard entry.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Delete Leaderboard Entry ---")

    player_id = input("Enter Player ID to delete: ")

    cur.execute("DELETE FROM Leaderboard WHERE PlayerID = %s", (player_id,))
    conn.commit()

    print('rows updated: ', cur.rowcount)

    if cur.rowcount == 1:
        print(f"Leaderboard entry for Player {player_id} deleted!")
    else:
        print('An error occurred deleting the leaderboard entry')

    cur.close()


def list_leaderboard(conn):
    """List all leaderboard entries.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- List Leaderboard ---")

    cur.execute("SELECT * FROM Leaderboard")
    records = cur.fetchall()

    if not records:
        print("No leaderboard entries found.")
        cur.close()
        return

    print(f"\n{'PlayerID':<15} {'Score':<10}")
    print("-" * 30)

    for record in records:
        print(f"{record['PlayerID']:<15} {record['Score']:<10}")

    cur.close()


def update_leaderboard_score(conn):
    """Update leaderboard score using the UpdateLeaderboardScore stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Update Leaderboard Score (Stored Procedure) ---")

    player_id = input("Enter Player ID: ")
    new_score = input("Enter new score: ")

    cur.callproc("UpdateLeaderboardScore", (player_id, new_score))
    conn.commit()

    print(f"Leaderboard score updated to {new_score}!")

    cur.close()

    git add .
git commit -m "Your commit message here"
git push origin main