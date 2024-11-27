import random
import string

import pytest
import requests
from faker import Faker

from constant import BASE_URL
from constant import HEADERS

fake = Faker()


@pytest.fixture(scope="session")
# авторизация
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    response = session.post(f"{BASE_URL}/auth", headers=HEADERS,
                            json={"username": "admin", "password": "password123"})
    print(response.status_code)
    assert response.status_code == 200, "Ошибка авторизации, статус не 200"
    token = response.json().get("token")
    assert token is not None, "Токена нет, ишак"
    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
# генерация данных
def booking_data():
    def _booking_data():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": fake.random_int(100, 1000000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2021-01-01",
                "checkout": "2023-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    return _booking_data()


@pytest.fixture()
def update_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(100, 1000000),
        "depositpaid": bool(random.getrandbits(1)),
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture()
def values_for_patch():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
    }


@pytest.fixture()
def negative_values_for_patch():
    return 0


@pytest.fixture()
def empty_data():
    return {
        "firstname": None,
        "lastname": None,
        "totalprice": [],
        "depositpaid": "",
        "bookingdates": {
            "checkin": None,
            "checkout": None
        },
        "additionalneeds": None
    }


@pytest.fixture()
def invalid_values(length=112):
    characters = string.ascii_letters + string.digits + string.punctuation
    values = ''.join(random.choice(characters) for _ in range(length))
    return values
