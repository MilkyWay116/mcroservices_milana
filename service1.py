import random
import time

from pet import Pet
from sql_queries import conn, create_table, insert_pet

create_table()

if __name__ == '__main__':
    while True:
        insert_pet(
                Pet(
                    name=random.choice(["Cтепа", "Кузя", "Маша", "Гоша", "Тиша"]),
                    view=random.choice(["млекопитающее", "рептилия", "птица"]),
                    age=random.randint(1,20),
                    illness=random.choice(["Грипп", "Простуда", "Лишай", "Кишечник", "Почки"]),
                    cost=0
                )
        )
        print("Inserted")
        time.sleep(10)
