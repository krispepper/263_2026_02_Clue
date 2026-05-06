# author: Madeline, 
# date: 4/19/2026
# Purpose: 263 application to work with game DB
#          connect to SQL 
#          manage main menu
# Changes by Kris Pepper

import mysql.connector

# everyone in the project shares app.py, 
#  but everyone should have their own 2 files: 
#    module to manage their table
#    module to run their queries

# module to manage a table
from player_manager import (
    player_manager_menu 
)

# module to manage a table for Deven
from Leaderboard_manager import (
    leaderboard_manager_menu
)

#module to mange a table for Madeline
from gamestatus_manager import (
    gamerun_manager_menu
)

#Player stats for gamerun queries
from stats_madelinestaley import(
    mplayer_stats_menu
)

#module to run queries
from player_status import (
    player_stats_menu
)

# Establish connection to database (edit accordingly)
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="devenbernardin",
    password="",
    database="madelinestaley",
)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Maintain Player")
        print("2. Monitor Game Run")
        print("3. Maintain Leaderboard")
        print("4. Game Run With Player Score Stats")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        match choice:
            case "1":
                player_manager_menu(conn)
            case "2":
                gamerun_manager_menu(conn)
            case "3":
                leaderboard_manager_menu(conn)
            case "4":
                mplayer_stats_menu(conn)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()