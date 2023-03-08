from sqlalchemy import create_engine
from pet import Pet
from sql_queries import insert_pet, number_of_pets, update_pet, get_pets


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    pet = Pet(
        name="Tom",
        view="млекопитающее",
        age=5,
        illness="test",
        cost=0,
    )

    insert_pet(conn, pet)
    pets = get_pets(conn)
    assert pets[3].name == "Tom"
    engine.dispose(conn_with_data)


def test_service2(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    update_pet(conn)
    pets = get_pets(conn)

    expected_costs = {
        'млекопитающее': 5000,
        'рептилия': 2000,
        'птица': 3000,
    }

    for pet in pets:
        assert pet.cost == expected_costs[pet.view]
    engine.dispose(conn_with_data)
#
#
def test_service4(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    pets = get_pets(conn)
    assert len(pets) == number_of_pets(conn)
    engine.dispose(conn_with_data)








