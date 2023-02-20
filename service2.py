import time
from sql_queries import create_table, update_pet

create_table()

if __name__ == '__main__':
    while True:
        update_pet()
        print("updated")
        time.sleep(10)
