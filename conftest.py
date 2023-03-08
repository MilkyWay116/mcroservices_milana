from sqlalchemy import Connection, create_engine
from sql_queries import insert_pet, create_table
from pet import Pet
from typing import Generator
import pytest
from testcontainers.postgres import PostgresContainer


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.get_container_host_ip = lambda: 'localhost'
        container.start()
        yield container

@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.get_container_host_ip = lambda: 'localhost'
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    pets = [
        Pet(
        name="test1",
        view="млекопитающее",
        age=5,
        illness="test",
        cost=0,
    ),
        Pet(
            name="test1",
            view="рептилия",
            age=4,
            illness="test",
            cost=0,
        ),
        Pet(
            name="test3",
            view="птица",
            age=2,
            illness="test",
            cost=0,
        )
    ]

    for pet in pets:
        insert_pet(conn, pet)

    return postgres_container.get_connection_url()




