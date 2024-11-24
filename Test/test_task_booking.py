from venv import create

import requests
import conftest
from constant import BASE_URL
from constant import HEADERS






class TestBooker:

    # создание бронирования
    def test_create_method(self, booking_data, get_token):
        create_booking = requests.get_token.post(f"{self.BASE_URL}/booking", headers=self.HEADERS, json=booking_data)
        assert create_booking.response.status == 200
        booking_id = create_booking.json.get("bookingid")
