import time
from sql_queries import create_table, update_pet

create_table(conn)

if __name__ == '__main__':
    while True:
        update_pet(conn)
        print("updated")
        time.sleep(10)
