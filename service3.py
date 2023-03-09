import time
from sql_queries import create_table, update_status
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        update_status(conn)
        print("updated")
        time.sleep(10)
