import mysql.connector

from test import get_date

#Establish connection
conn = mysql.connector.connect(host = "127.0.0.1", port = 3306, user = "madelinestaley", password = "", database = "madelinestaley")

def main():
    get_date(conn)
    conn.close()
    if __name__ == "__main__": main()