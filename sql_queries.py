from psycopg2.extensions import connection
from sqlalchemy.engine import Connection
from sqlalchemy import text


from pet import Pet


def create_table(conn: Connection):
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

    conn.execute(text(query))
    conn.commit()


def insert_pet(conn: Connection, pet: Pet):
    query = """
            INSERT INTO vet_clinic_milana
            (name, view, age, illness, cost)
            VALUES (:name, :view, :age, :illness, :cost)
            """
    conn.execute(
        text(query),
        parameters={"name": pet.name,
                    "view": pet.view,
                    "age": pet.age,
                    "illness": pet.illness,
                    "cost": pet.cost,
                    }
                 )
    conn.commit()


def update_pet(conn: Connection):
    query = """
    UPDATE vet_clinic_milana SET cost= CASE WHEN view = 'млекопитающее' THEN 5000
    WHEN view = 'рептилия' THEN 2000 WHEN view = 'птица' THEN 3000 END;
    """

    conn.execute(text(query))
    conn.commit()

def update_status(conn: Connection):
    query = """
    UPDATE vet_clinic_milana SET status = vet_clinic2_milana.status FROM vet_clinic2_milana 
    WHERE vet_clinic_milana.id = vet_clinic2_milana.id 
    """
    conn.execute(text(query))
    conn.commit()

def number_of_pets(conn: Connection) -> list[Pet]:
    query = "SELECT COUNT(name) FROM vet_clinic_milana;"
    conn.execute(text(query))
    return conn.execute(text(query)).fetchone()[0]
    # return cursor.fetchone()[0]


def get_pets(conn: Connection) -> list[Pet]:
    query = "SELECT * FROM vet_clinic_milana;"
    # print("ddd")
    pets = conn.execute(text(query)).fetchall()
    # print("ddd1")
    return [Pet(
        id=pet[0],
        name=pet[1],
        view=pet[2],
        age=pet[3],
        illness=pet[4],
        cost=pet[5],
        created=pet[6],
        status=pet[7],
    ) for pet in pets]



