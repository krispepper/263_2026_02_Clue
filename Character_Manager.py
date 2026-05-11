# author: Davyne Walker 
# date: 4/22/2026
# Purpose: Present a table that lists the details of character roles and advantages

def characters_manager_menu(conn):
    ''' This handles the menu of all the options to maintain the table
        You will be changing 'Player' to the name of your table. 
    args: 
        conn: Active MySQL database connection
    '''
    print("\n--- Characters ---")
    print("1. Add Character")
    print("2. Change Character")
    print("3. Delete Character")
    print("4. List Characters")
    print("5. List Board Data")
    print("6. List End game Results")
    print("7. List player win/loss history")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            add_character(conn)
        case "2":
            change_character(conn)
        case "3":
            delete_character(conn)
        case "4":
            list_characters(conn)
        case "5":
            list_board_for_game(conn)
        case "6":
            list_end_game_results(conn)
        case "7":
            list_player_winloss_history(conn)
        case _:
            print("Invalid choice. Please try again.")

def add_character(conn):
    """Add a new character to the database. 
       You will add a new record to your table
    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    cur = conn.cursor()
    # Prompt user for character info
    newName = input("What is this character's name? ").strip()
    newRole = input("What is their role? ").strip()
    newAge = input("How old are they? ").strip()
    newGender = input("What is their gender (M/F)? ").strip()
    newHeight = input("What is their height (cm)? ").strip()
    newRoutine = input("What is their routine? ").strip()
    # Write INSERT query to add a new record
    cur.execute(f"INSERT INTO Role(CharacterRole) VALUES('{newRole}')")
    cur.execute(f"INSERT INTO Characters(CharacterName, CharacterRole, Age, Gender, Height, Routine) VALUES('{newName}', '{newRole}', '{newAge}', '{newGender}', '{newHeight}', '{newRoutine}')")
    # Commit the transaction
    conn.commit()
    # Check for success and print update message
    print ("Rows updated: ", cur.rowcount)
    if cur.rowcount == 1:
        print(f"Character added successfully!")
    else:
        print("An error occurred adding character")

    cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{newName}'")
    row = cur.fetchone()
    print("\nYou have added the new character: ")
    print(row)
    # Close the cursor
    conn.close()
    pass


def change_character(conn):
    """Update player information in database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    cur = conn.cursor()
    # Prompt user for character to change
    print("\n--- Characters ---")
    cur.execute("SELECT CharacterName FROM Characters")
    row = cur.fetchall()
    print(row)
    characterChoice = input("Which character are you changing: ").strip()
    # Write SELECT query to fetch player data
    # If player not found, print message and return
    # Display current player data
    cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
    character = cur.fetchone()
    if not character:
        print("Invalid choice, please try again")
        cur.close()
        return
    
    
    print("Character information: ")
    print(character)

    # Print menu of fields to change (1-5):
    print("\n--- Options ---")
    print("1. Name")
    print("2. Role")
    print("3. Age")
    print("4. Gender")
    print("5. Height")
    print("6. Routine")
    # Prompt user for field choice
    changeChoice = input("Which do you want to change (1-6): ").strip()
    # If invalid choice, print message and return
    match changeChoice:
        case "1":
            cur.execute(f"SELECT CharacterName FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character name: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change: ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET CharacterName = '{newChange}' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character name updated successfully!")
            else:
                print("An error occurred updating character") 

            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{newChange}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case "2":
            cur.execute(f"SELECT CharacterRole FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character role: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change: ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET CharacterRole = '{newChange}' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character role updated successfully!")
            else:
                print("An error occurred updating character") 

            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case "3":
            cur.execute(f"SELECT Age FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character age: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change: ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET Age = '{newChange}' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character age updated successfully!")
            else:
                print("An error occurred updating character") 

            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case "4":
            cur.execute(f"SELECT Gender FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character gender: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change: ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET Gender = '{newChange}' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character gender updated successfully!")
            else:
                print("An error occurred updating character") 

            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case "5":
            cur.execute(f"SELECT Height FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character height: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change (cm): ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET Height = '{newChange} cm' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character height updated successfully!")
            else:
                print("An error occurred updating character") 

            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case "6":
            cur.execute(f"SELECT Routine FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print("Current character routine: ", row)
            # Prompt user for new value for selected field
            newChange = input("Enter the change: ").strip()
            # Write UPDATE query to modify only that field
            cur.execute(f"UPDATE Characters SET Routine = '{newChange}' WHERE characterName = '{characterChoice}'")
            # Commit the transaction
            conn.commit()
            # Check for success and print update message
            print ("Rows updated: ", cur.rowcount)
            if cur.rowcount == 1:
                print(f"Character routine updated successfully!")
            else:
                print("An error occurred updating character") 
            
            cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{characterChoice}'")
            row = cur.fetchone()
            print(f"\nNew character information for this character: ")
            print(row)
        case _:
            print("Invalid choice. Try again")
            return    
    # Close the cursor
    cur.close()


def delete_character(conn):
    """Delete a player from the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    cur = conn.cursor()
    # Prompt user for character to delete
    cur.execute("SELECT CharacterName FROM Characters")
    row = cur.fetchall()
    print(row)
    deleteChoice = input("\nWho do you want to delete? ")

    cur.execute(f"SELECT * FROM Characters WHERE CharacterName = '{deleteChoice}'")
    character = cur.fetchone()
    if not character:
        print("Invalid choice, please try again")
        cur.close()
        return
    
    # Write DELETE query to remove the player
    cur.execute(f"DELETE FROM Characters WHERE CharacterName = '{deleteChoice}'")
    # Commit the transaction
    conn.commit()
    # Check for success and Print deletion message
    print ("Rows updated: ", cur.rowcount)
    if cur.rowcount == 1:
        print(f"Character deleted successfully!")
    else:
        print("An error occurred deleting character") 
    # Close the cursor
    cur.close()

def list_characters(conn):
    """List all characters in the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Character List ---")
    cur.execute("SELECT CharacterName, CharacterRole, Age, Gender, Height, Coalesce(Routine, 'Currently unavailable') AS Routine FROM Characters")
    characters = cur.fetchall()

    if not characters:
        print("No characters found.")
        cur.close()
        return

    print(
        f"\n{'CharacterName':<20} {'CharacterRole':<15} {'Age':<3} {'Gender':<10} {'Height':<10} {'Routine':<200}"
    )
    print("-" * 80)
    for character in characters:
        print(
            f"{character['CharacterName']:<20} {character['CharacterRole']:<15} {character['Age']:<3} {character['Gender']:<10} {character['Height']:<10} {character['Routine']:<200}"
        )

    cur.close()

def list_board_for_game(conn):
    """ List the current board data for a given game """

    # Ask for game number 
    gameNumber = input("What is the game number you would like to see? ").strip()

    # Activate cursor
    cur = conn.cursor(dictionary=True)

    print("\n--- TIles List With Players On Them ---")
    cur.execute(f"SELECT Board.RoomID, Board.Tiles, COALESCE(GamerunPlayers.PlayerNumber, 'Vancant') AS PlayerNumber, \
        COALESCE(CharacterName, '') AS CharacterName, COALESCE(GameID, '') AS GameID, RoomType FROM GamerunPlayers \
        RIGHT JOIN Board on GamerunPlayers.RoomID = Board.RoomID \
        AND GamerunPlayers.Tiles = Board.Tiles \
        JOIN Room ON Board.RoomID = Room.RoomID \
        LEFT JOIN Players ON GamerunPlayers.PlayerNumber = Players.PlayerNumber \
        WHERE GameID IS NULL OR GameID = '{gameNumber}'")
    characters = cur.fetchall()

    if not characters:
        print("No characters found.")
        cur.close()
        return
    

    print(
        f"\n{'RoomID':<8} {'Tiles':<8} {'PlayerNumber':<14} {'CharacterName':<20} {'GameID':<8} {'RoomType':<20}"
    )
    print("-" * 80)
    for character in characters:
        print(
            f"{character['RoomID']:<8} {character['Tiles']:<8} {character['PlayerNumber']:<14} {character['CharacterName']:<20} {character['GameID']:<8} {character['RoomType']:<20}"
        )

    cur.close()

def list_end_game_results(conn):
    # Activate cursor
    cur = conn.cursor(dictionary=True)

    # Execute query
    cur.execute("SELECT gp.GameID, Status, PlayerNumber, Score, CASE WHEN maxscore = score THEN 'Winner' ELSE 'Loser' END AS Result \
    , CASE WHEN maxscore = score THEN 1 ELSE 0 END AS WinCount \
    FROM GamerunPlayers gp \
    JOIN (SELECT GameID, max(score) as maxscore \
    FROM GamerunPlayers g \
	GROUP BY GameID) mg \
	ON gp.GameID = mg.GameID \
    WHERE CASE WHEN maxscore = score THEN 'Winner' ELSE 'Loser' END = 'Winner' AND Status = 'Completed' \
     ORDER BY GameID")
    results = cur.fetchall()

    if not results:
        print("All games are either in progress, or have yet to be started. Please try again later.")
        cur.close()
        return

     # GameID, Status, PlayerNumber, Score, Result, WinCount
    print(
    f"\n{'GameID':<8} {'Status':<12} {'PlayerNumber':<14} {'Score':<8} {'Result':<10} {'WinCount':<10}"
    )
    print("-" * 80)
    for result in results:
        print(
        f"{result['GameID']:<8} {result['Status']:<12} {result['PlayerNumber']:<14} {result['Score']:<8} {result['Result']:<10} {result['WinCount']:<10}"
        )
        
    cur.close()

def list_player_winloss_history(conn):
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT PlayerNumber, sum( CASE WHEN maxscore = score THEN 1 ELSE 0 END) AS TotalWins \
    , sum( CASE WHEN maxscore = score THEN 0 ELSE 1 END) AS TotalLoses \
    FROM GamerunPlayers gp \
    JOIN (SELECT GameID, max(score) as maxscore \
    FROM GamerunPlayers g GROUP BY GameID) mg \
    ON gp.GameID = mg.GameID \
    GROUP BY PlayerNumber")
    characters = cur.fetchall()

    if not characters:
        print("There is currently no win/loss history for these players yet.")
        cur.close()
        return
    
    # PlayerNumber, TotalWins, TotalLoses

    print(
        f"\n{'PlayerNumber':<15} {'TotalWins':<12} {'TotalLoses':<12}"
    )
    print("-" * 80)
    for character in characters:
        print(
            f"{character['PlayerNumber']:<15} {character['TotalWins']:<12} {character['TotalLoses']:<12}"
        )
    cur.close()