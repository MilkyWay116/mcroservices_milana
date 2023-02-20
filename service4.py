import time
from sql_queries import create_table, number_of_pets

create_table()

if __name__ == '__main__':
    while True:
        number = number_of_pets()
        print("Число пациентов-животных:", str(number))
        time.sleep(10)
