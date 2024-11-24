import pytest
import requests
from faker import Faker

fake = Faker()
BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


@pytest.fixture(scope="session")
# авторизация
def auth_token():
    session = requests.Session()
    session.headers.update(HEADERS)
    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS,
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
