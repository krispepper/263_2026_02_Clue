# author: Nikolaos Komninos 
# date: 4/19/2026
# Purpose: present a menu to manage a table 
#     add/update/delete/list the table
# Changes by Kris Pepper

def player_manager_menu(conn):
    ''' This handles the menu of all the options to maintain the table
        You will be changing 'Player' to the name of your table. 
    args: 
        conn: Active MySQL database connection
    '''
    print("\n--- Maintain Player ---")
    print("1. Add Player")
    print("2. Change Player")
    print("3. Delete Player")
    print("4. List Players")
    print("5. Update Player Score (Stored Procedure)")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            add_player(conn)
        case "2":
            change_player(conn)
        case "3":
            delete_player(conn)
        case "4":
            list_players(conn)
        case "5":
            update_player_score(conn)
        case _:
            print("Invalid choice. Please try again.")

def add_player(conn):
    """Add a new player to the database. 
       You will add a new record to your table
    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for: Player ID, Name, Color, Wins, Losses, Gold
    #  You will prompt the user for the values you need to insert
    # Write INSERT query to add a new record
    # Commit the transaction
    # Check for success and Print success message
    # Close the cursor
    pass


def change_player(conn):
    """Update player information in database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID to change
    # Write SELECT query to fetch player data
    # If player not found, print message and return
    # Display current player data
    # Print menu of fields to change (1-5):
    #   1. Name
    #   2. Color
    #   3. Wins
    #   4. Losses
    #   5. Gold
    # Prompt user for field choice
    # If invalid choice, print message and return
    # Map choice to field name using a dictionary
    # Prompt user for new value for selected field
    # Write UPDATE query to modify only that field
    # Commit the transaction
    # Check for success and Print success message
    # Close the cursor
    pass


def delete_player(conn):
    """Delete a player from the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID to delete
    # Write DELETE query to remove the player
    # Commit the transaction
    # Check for success and Print deletion message
    # Close the cursor
    pass


def list_players(conn):
    """List all players in the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Write SELECT query to fetch all players
    # If no players found, print message and return
    # Print header row with column names
    # Loop through results and print each player
    # Close the cursor
    pass


def update_player_score(conn):
    """Update a player's wins using UpdatePlayerScore stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID and new number of wins
    # Call the UpdatePlayerScore stored procedure using cur.callproc()
    # Commit the transaction
    # Print success message
    # Close the cursor
    pass