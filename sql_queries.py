import psycopg2
import time

from pet import Pet

conn = psycopg2.connect(
    host='test.dsacademy.kz',
    database='fortesting',
    user='testing',
    password='testing123'
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS vet_clinic_milana (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL, 
    view VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    illness VARCHAR(255) NOT NULL,
    cost INTEGER,
    created DATE DEFAULT NOW(),
    status VARCHAR(255) DEFAULT 'not paid')
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_pet(pet: Pet):
    query = """
            INSERT INTO vet_clinic_milana
            (name, view, age, illness, cost)
            VALUES (%s, %s, %s, %s,%s)
            """
    cursor = conn.cursor()
    cursor.execute(query, (pet.name, pet.view, pet.age, pet.illness, pet.cost))
    conn.commit()


def update_pet():
    query = """
    UPDATE vet_clinic_milana SET cost= CASE WHEN view = 'млекопитающее' THEN 5000
    WHEN view = 'рептилия' THEN 2000 WHEN view = 'птица' THEN 3000 END;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def update_status():
    query = """
    UPDATE vet_clinic_milana SET status = vet_clinic2_milana.status FROM vet_clinic2_milana 
    WHERE vet_clinic_milana.id = vet_clinic2_milana.id 
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def number_of_pets() -> list[Pet]:
    query = "SELECT COUNT(name) FROM vet_clinic_milana;"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()[0]
