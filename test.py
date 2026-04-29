def get_date(conn):

    cur = conn.cursor()
    cur.execute("SELECT CURDATE() as CurrentDate")
    row = cur.fetchcone()
    print(f"Current date is: {row[0]}")