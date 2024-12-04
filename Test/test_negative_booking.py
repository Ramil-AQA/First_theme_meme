from assertpy import assert_that

from constant import BASE_URL


class TestNegativeBooking:
    def test_get_negative(self,auth_session, generation, invalid_values):

        get_different_value = auth_session.get(f"{BASE_URL}/booking/{generation}")
        assert_that(get_different_value.status_code).is_equal_to(404), "Ошибка, статус должен быть 404"
        # теперь для невалидных
        get_invalid_value = auth_session.get(f"{BASE_URL}/booking/{invalid_values}")
        assert_that(get_invalid_value.status_code).is_equal_to(404), "Ошибка, статус должен быть 404"


    def test_put_method(self, auth_session, booking_data, empty_values_for_method, generation):
        create_booking = auth_session.post(f"{BASE_URL}/booking",
                                       json=(booking_data()))
        data = create_booking.json().get('bookingid')
        update_booking = auth_session.put(f"{BASE_URL}/booking/{data}", json=empty_values_for_method)
        assert_that(update_booking.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"
        update_booking_invalid_obj = auth_session.put(f"{BASE_URL}/booking/{generation}",
                                                  json=empty_values_for_method)
        assert_that(update_booking_invalid_obj.status_code).is_equal_to(400), "Ошибка, статус должен быть 400"

    def test_patch_method(self, booking_data, auth_session, empty_values_for_method):
        create_booking = auth_session.post(f"{BASE_URL}/booking",
                                       json=booking_data())
        data = create_booking.json().get('bookingid')
        patch_booking_method = auth_session.patch(f"{BASE_URL}/booking/{data}", json=empty_values_for_method)
        assert_that(patch_booking_method.status_code).is_equal_to(200), "Ошибка, статус должен быть 200"
        delete_booking_patch = auth_session.delete(f"{BASE_URL}/booking/{data}")
        assert_that(delete_booking_patch.status_code).is_equal_to(201)
        get_deleted_booking_patch = auth_session.get(f"{BASE_URL}/booking/{data}")
        assert_that(get_deleted_booking_patch.status_code).is_equal_to(404), "Букинг не был удален"
