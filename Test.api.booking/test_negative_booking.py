import pytest
from assertpy import assert_that

from constant import BASE_URL


class TestNegativeBooking:
    @pytest.mark.parametrize(
        "value",
        (0, "long")
    )
    def test_get_booking_id_by_not_found(self, auth_session, value, invalid_values):
        if value == "long": value = invalid_values
        get_different_value = auth_session.get(f"{BASE_URL}/booking/{value}")
        assert_that(get_different_value.status_code).is_equal_to(404), "Ошибка, статус должен быть 404"

    def test_put_method(self, auth_session, booking_data, new_booking):
        booking_id, booking_data = new_booking()

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json={})
        assert_that(update_booking.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"

    @pytest.mark.parametrize(
        "value",
        (0, "long")
    )
    def test_put_is_not_exist_booking(self, auth_session, invalid_values, value):
        if value == "long": value = invalid_values
        update_booking = auth_session.put(f"{BASE_URL}/booking/{value}", json={})
        assert_that(update_booking.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"

    def test_patch_method(self, booking_data, auth_session, new_booking):
        booking_id, booking_data = new_booking()

        patch_booking_method = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={ })
        assert_that(patch_booking_method.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"

"""
    def test_patch_after_delete(self, auth_session, new_booking, booking_data):
        booking_id, booking_data = new_booking()

        self.test_patch_method(booking_data, auth_session, new_booking)

        get_deleted_booking_patch = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        delete_booking_patch = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert_that(get_deleted_booking_patch.status_code).is_equal_to(404), "Букинг не был удален"
"""