import random

import pytest
import requests
from assertpy import assert_that
from faker import Faker

from constant import HEADERS
from sql_pokemons.constant import BASE_URL
from sql_pokemons.db import row_query

fake = Faker('EN')


@pytest.fixture
def auth_sessions():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


@pytest.fixture
def pokemon_data():
    def _pokemon_data():
        photo_id = str(random.randint(1, 1008))
        return {
            'name': fake.first_name(),
            'photo_id': photo_id
        }

    return _pokemon_data()


@pytest.fixture
def create_pokemon(pokemon_data, auth_sessions):
    pokemon_id = None

    def _create_pokemon():
        nonlocal pokemon_id
        data = pokemon_data
        create_post_request_for_pokemon = auth_sessions.post(f"{BASE_URL}/pokemons", json=data)
        assert_that(create_post_request_for_pokemon.status_code).is_equal_to(201)
        pokemon_id = create_post_request_for_pokemon.json().get('id')
        assert pokemon_id is not None, 'Айдишки нет, перепроверь тест'
        return create_post_request_for_pokemon.json(), data

    return _create_pokemon()
    throw_pokemon = row_query(f'SELECT status FROM public.pokemons WHERE id = {pokemon_id}')
    if throw_pokemon == {"status": 1}:
        knockout_pokemon = auth_sessions.post(f'{BASE_URL}/pokemons/knockout', json={"pokemon_id": pokemon_id})
        assert_that(knockout_pokemon.status_code).is_equal_to(200)
    else:
        assert_that(throw_pokemon[0]).contains_entry(
            {'status':1}
        )


@pytest.fixture
def add_in_pokeball(auth_sessions, create_pokemon):
    response, data = create_pokemon
    pokemon_id = response.get('id')
    add_in_pokeball = auth_sessions.post(f"{BASE_URL}/trainers/add_pokeball", json={"pokemon_id": pokemon_id})
    assert_that(add_in_pokeball.status_code).is_equal_to(200)
    return pokemon_id


@pytest.fixture
def choose_pokemon_id():
    def _choose_pokemon_id():
        table_data = row_query(f'SELECT * FROM public.pokemons')
        return random.choice(table_data)

    return _choose_pokemon_id


@pytest.fixture
def enemy_pokemon():
    pokemons = row_query(f'SELECT * FROM public.pokemons WHERE "in_pokeball" = 1 AND NOT "trainer_id" = 27241')
    random_pokemons = random.choice(pokemons)
    return random_pokemons
