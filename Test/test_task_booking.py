from constant import BASE_URL


class TestBooker:

    # создание бронирования
    def test_create_method(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга нет в ответе"
        booking_get = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert booking_get.status_code == 200, "Ошибка, статус должен быть 200"
        data_booking = booking_get.json()
        assert data_booking['firstname'] == booking_data['firstname'], 'ИМЯ НЕ СОВПАДАЕТ'
        assert data_booking['lastname'] == booking_data['lastname'], 'фамилия НЕ СОВПАДАЕТ'
        assert data_booking['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert data_booking['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert data_booking['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert data_booking['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"
