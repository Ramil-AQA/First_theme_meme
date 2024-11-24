import requests
BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


class TestBooker:

    # создание бронирования
    def test_create_method(self, booking_data, auth_token):
        create_booking = auth_token.post(f"{BASE_URL}/booking", headers=HEADERS, json=booking_data)
        assert create_booking.response.status == 200
        booking_id = create_booking.json.get("bookingid")
        assert booking_id is not None, "ID букинга нет в ответе"
