import time
from sql_queries import create_table, number_of_pets
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        number = number_of_pets(conn)
        print("Число пациентов-животных:", str(number))
        time.sleep(10)
