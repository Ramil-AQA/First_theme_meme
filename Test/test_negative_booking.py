import random

from assertpy import assert_that

from Test.test_positive_booking import TestBooker
from constant import BASE_URL


class TestNegative_booking(TestBooker):
    # для get запроса, проверка несуществующих айдишников
    def test_get_negative(self, empty_data, auth_session, invalid_values):
        get_different_value = auth_session.get(f"{BASE_URL}/booking/{random.randint(-1111111111, 999999999999)}")
        assert_that(get_different_value.status_code).is_equal_to(404), "Ошибка, статус должен быть 404"
        # теперь для невалидных
        get_invalid_value = auth_session.get(f"{BASE_URL}/booking/{invalid_values}")
        assert_that(get_invalid_value.status_code).is_equal_to(404), "Ошибка, статус должен быть 404"

    def test_put_method(self, auth_session, booking_data, empty_data, update_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking",
                                           json=booking_data)
        data = create_booking.json().get('bookingid')
        update_booking = auth_session.put(f"{BASE_URL}/booking/{data}", json=empty_data)
        assert_that(update_booking.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"
        update_booking_invalid_obj = auth_session.put(f"{BASE_URL}/booking/{random.randint(-1111111111, 999999999999)}", json=empty_data)
        assert_that(update_booking_invalid_obj.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"
    def test_patch_method (self, booking_data, auth_session, update_data, negative_values_for_patch):
        create_booking = auth_session.post(f"{BASE_URL}/booking",
                                           json=booking_data)
        data = create_booking.json().get('bookingid')
        patch_booking_method = auth_session.patch(f"{BASE_URL}/booking/{data}", json=negative_values_for_patch)
        assert_that(patch_booking_method.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"
        delete_booking_patch = auth_session.delete(f"{BASE_URL}/booking/{data}")
        get_deleted_booking_patch = auth_session.get(f"{BASE_URL}/booking{data}")
        assert_that(get_deleted_booking_patch.status_code).is_equal_to(404), "Букинг не был удален"
