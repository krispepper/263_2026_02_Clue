# author: Nikolaos Komninos 
# date: 4/19/2026
# Purpose: present a menu to list queries 
# Changes by Kris Pepper

def player_stats_menu(conn):
    ''' This handles the menu of all the options to print player stats
        You will be changing all the menu options to reflect the queries
           you are running.  
    args: 
        conn: Active MySQL database connection
    '''
    print("\n--- Player Reports ---")
    print("1. Player Statistics (Stored Procedure)")
    print("2. Players Grouped by Wins (GROUP BY)")
    print("3. Players with Gold Above Average (Sub-query)")
    print("4. High-Winning Players (HAVING)")
    print("5. All Players with Stats (LEFT OUTER JOIN)")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            query_player_stats(conn)
        case "2":
            query_players_by_wins(conn)
        case "3":
            query_players_by_gold(conn)
        case "4":
            query_top_players(conn)
        case "5":
            query_all_players_with_stats(conn)
        case _:
            print("Invalid choice. Please try again.")

def query_player_stats(conn):
    """Query player statistics using GetPlayerStats stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Call the GetPlayerStats stored procedure using cur.callproc()
    # Loop through stored results
    # Print each statistic: TotalPlayers, TotalWins, TotalLosses, AverageGold, MaxWins
    # Close cursor
    pass


def additional_query_1(conn):
    """Additional query 1 - GROUP BY.

    Args:
        conn: Active MySQL database connection
    """
    # GROUP BY
    # Create a cursor with dictionary=True
    # Write a SELECT query using GROUP BY
    # Print header row
    # Loop through results and print each player
    # Close cursor
    pass


def additional_query_2(conn):
    """Additional query 2 - Sub-query.

    Args:
        conn: Active MySQL database connection
    """
    # Sub-query
    # Create a cursor with dictionary=True
    # Write a SELECT query using a sub-query
    # Print header row
    # Loop through results and print each player
    # Close cursor
    pass


def additional_query_3(conn):
    """Additional query 3 - HAVING.

    Args:
        conn: Active MySQL database connection
    """
    # HAVING
    # Create a cursor with dictionary=True
    # Write a SELECT query using HAVING
    # Print header row
    # Loop through results and print each player
    # Close cursor
    pass


def additional_query_4(conn):
    """Additional query 4 - LEFT OUTER JOIN.

    Args:
        conn: Active MySQL database connection
    """
    # LEFT OUTER JOIN
    # Create a cursor with dictionary=True
    # Write a SELECT query using LEFT OUTER JOIN
    # Print header row
    # Loop through results and print each player
    # Close cursor
    pass