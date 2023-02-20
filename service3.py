import time
from sql_queries import create_table, update_status

create_table()

if __name__ == '__main__':
    while True:
        update_status()
        print("updated")
        time.sleep(10)
