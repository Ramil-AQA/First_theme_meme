import pytest
from assertpy import assert_that

from constant import BASE_URL


class TestBooker:

    # создание бронирования
    def test_create_method(self, booking_data, auth_session):
        data = booking_data()
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=data)
        assert_that(create_booking.status_code).is_equal_to(200)
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга нет в ответе"
        booking_get = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert_that(booking_get.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"
        assert_that(data).is_equal_to(booking_get.json())

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert_that(delete_booking.status_code).is_equal_to(201), f"Ошибка при удалении букинга с ID {booking_id}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking{booking_id}")
        assert_that(get_deleted_booking.status_code).is_equal_to(404), "Букинг не был удален"

    # изменяем бронирование
    def test_update_method(self, booking_data, auth_session, new_booking):
        booking_id, old_data = new_booking()
        new_data = booking_data()

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=new_data)
        assert_that(update_booking.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"

        booking_get = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert_that(booking_get.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"
        assert_that(booking_get.json()).is_not_equal_to(old_data)
        assert_that(booking_get.json()).is_equal_to(new_data)

    # частично изменяем бронирование
    @pytest.mark.parametrize(
        argnames='key',
        argvalues=['firstname', 'lastname']
    )
    def test_patch_method(self, booking_data, auth_session, new_booking, key):
        booking_id, data = new_booking()
        new_property = {key: 'ZZZ'}
        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=new_property)
        assert_that(patch_booking.status_code).is_equal_to(200)
        assert_that(patch_booking.json()).is_not_equal_to(data)
        del data[key]
        data.update(new_property)
        assert_that(patch_booking.json()).is_equal_to(data)