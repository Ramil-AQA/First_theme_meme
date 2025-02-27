from datetime import timedelta, datetime

import pytest
from assertpy import assert_that
from faker.proxy import Faker

fake = Faker('EN')
from db import row_query
from sql_pokemons.conftest import auth_sessions, pokemon_data, choose_pokemon_id, create_pokemon
from sql_pokemons.constant import BASE_URL


class TestPokemon:
    def test_create_pokemon(self, create_pokemon):
        response, data = create_pokemon
        assert_that(response.get('message')).is_equal_to('Покемон создан')
        pokemon_id = response.get('id')
        table_data = row_query(f"SELECT * FROM public.pokemons WHERE id = '{pokemon_id}'")
        assert_that(table_data).is_length(1)
        assert_that(table_data[0]).contains_entry(
            {'id': int(pokemon_id)},
            {'name': data.get('name')},
            {'stage': 1},
            {'win_count': 0},
            {'attack': 1},
            {'trainer_id': 25764},
            {'status': 1},
            {'in_pokeball': 0},
            {'photo_id': int(data.get('photo_id'))}
        )
        create_date = table_data[0].get('create_date')
        datetime_now = datetime.now() - timedelta(hours=3)
        data_start = datetime_now - timedelta(seconds=10)
        data_end = datetime_now + timedelta(seconds=10)
        assert_that(create_date).is_before(data_end)
        assert_that(create_date).is_after(data_start)

    def test_put_pokemons(self, auth_sessions, create_pokemon, pokemon_data):
        response, data = create_pokemon()
        assert_that(response.get('message')).is_equal_to('Покемон создан')
        new_data = pokemon_data()
        pokemon_id = response.get('id')
        new_data['pokemon_id'] = pokemon_id
        new_pokemons = auth_sessions.put(f'{BASE_URL}/pokemons', json=new_data)
        assert_that(new_pokemons.status_code).is_equal_to(200)
        new_response = new_pokemons.json()
        assert_that(new_response.get('message')).is_equal_to('Информация о покемоне обновлена')
        table_data = row_query(f"SELECT * FROM public.pokemons WHERE id = '{pokemon_id}'")
        assert_that(new_response).is_not_equal_to(data)
        assert_that(table_data[0]).contains_entry(
            {
                'id': int(pokemon_id)
            },
            {
                'name': new_data['name']
            },
            {
                'photo_id': int(new_data['photo_id'])
            }
        )


    @pytest.mark.parametrize(
        "key",
        [
            "photo_id",
            "name"
        ]
    )
    def test_patch_pokemons(self, create_pokemon, auth_sessions, pokemon_data, key):
        response, data = create_pokemon()
        pokemon_id = response.get('id')
        new_data = pokemon_data()
        patch_pokemon = auth_sessions.patch(f"{BASE_URL}/pokemons", json={
            "pokemon_id": pokemon_id,
            key: new_data[key]
        })
        assert_that(patch_pokemon.status_code).is_equal_to(200)
        db_data = row_query(f'SELECT * FROM public.pokemons WHERE id = {pokemon_id}')
        assert_that(str(db_data[0].get(key))).is_equal_to(new_data[key])
        assert_that(str(db_data[0].get(key))).is_not_equal_to(data[key])

    def test_add_pokemon_in_pokeball(self, auth_sessions, add_in_pokeball, create_pokemon):
        response, data = create_pokemon()
        pokemon_id = response.get('id')
        add_in_pokeball = auth_sessions.post(f"{BASE_URL}/trainers/add_pokeball", json={"pokemon_id": str(pokemon_id)})
        db_data = row_query(f"SELECT * FROM public.pokemons WHERE id = '{pokemon_id}'")
        assert_that(add_in_pokeball.status_code).is_equal_to(200)
        assert_that(db_data[0]).contains_entry(
            {'in_pokeball': 1}
        )

    def test_post_battle_pokemons(self, create_pokemon, auth_sessions, enemy_pokemon, add_in_pokeball):
        my_pokemon = add_in_pokeball()
        defending_pokemon = enemy_pokemon().get('id')
        battle = auth_sessions.post(f"{BASE_URL}/battle", json={
            "attacking_pokemon": str(my_pokemon),
            "defending_pokemon": str(defending_pokemon)
        })
        assert_that(battle.status_code).is_equal_to(200)
        print(battle.json().get('result'))
        print(battle.json().get('id'))
        assert_that(battle.json().get('message')).is_equal_to('Битва проведена')
        assert_that(battle.json()).is_not_empty()
        if battle.json().get('result') == 'Твой покемон победил':
            assert_that(battle.json().get('result')).is_equal_to('Твой покемон победил')
        else:
            assert_that(battle.json().get('result')).is_equal_to('Твой покемон проиграл')
        battle_data = row_query(f"SELECT * FROM public.battles WHERE id = '{battle.json().get('id')}'")
        assert_that(battle_data[0]).contains_entry(
            {
                'id': int(battle.json().get('id'))
            }
        )
