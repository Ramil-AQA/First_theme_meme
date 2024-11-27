from assertpy import assert_that

from constant import BASE_URL


class TestBooker:

    # создание бронирования
    def test_create_method(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert_that(create_booking.status_code).is_equal_to(200)
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга нет в ответе"
        booking_get = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert_that(booking_get.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert_that(delete_booking.status_code).is_equal_to(201), f"Ошибка при удалении букинга с ID {booking_id}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking{booking_id}")
        assert_that(get_deleted_booking.status_code).is_equal_to(404), "Букинг не был удален"

    # изменяем бронирование
    def test_update_method(self, booking_data, auth_session, update_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert_that(create_booking.status_code).is_equal_to(200)
        data = create_booking.json().get('bookingid')
        update_booking = auth_session.put(f"{BASE_URL}/booking/{data}", json=update_data)
        auth_session.put(f"{BASE_URL}/booking/{data}", json=update_data)
        assert_that(update_booking.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{data}")
        assert_that(delete_booking.status_code).is_equal_to(201), f"Ошибка при удалении букинга с ID {data}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking{data}")
        assert_that(get_deleted_booking.status_code).is_equal_to(404), "Букинг не был удален"
        #наверное еще стоит добавить проверку, когда мы изменяем на пустой объект (??)

    # полностью изменяем бронирование
    def test_patch_method(self, booking_data, auth_session, update_data):
        create_booking_for_patch = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert_that(create_booking_for_patch.status_code).is_equal_to(200)
        data_for_patch = create_booking_for_patch.json().get('bookingid')
        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{data_for_patch}", json=update_data)
        assert_that(patch_booking.status_code).is_equal_to(200)
        delete_booking_patch = auth_session.delete(f"{BASE_URL}/booking/{data_for_patch}")
        assert_that(delete_booking_patch.status_code).is_equal_to(
            201), f"Ошибка при удалении букинга с ID {data_for_patch}"
        get_deleted_booking_patch = auth_session.get(f"{BASE_URL}/booking{data_for_patch}")
        assert_that(get_deleted_booking_patch.status_code).is_equal_to(404), "Букинг не был удален"
