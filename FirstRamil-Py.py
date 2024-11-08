from datetime import datetime
order = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T21:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T21:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-01T16:17:04.723Z",
            "completedAt": "2024-03-22T22:17:04.723Z2",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}
### 1 задание : Надо убедиться, что заказы вообще есть в ответе от сервера
assert len(order["data"]) > 0, "Заказы отсутствуют"
### конец первого задания
### 2 задание: Надо убедиться, что время выполнение первого и второго заказов не превышает
started_1 = datetime.strptime(order["data"][0]["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
completed_1 = datetime.strptime(order["data"][0]["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
difference_time_0 = (completed_1 - started_1).seconds
print(difference_time_0)
started_2 = datetime.strptime(order["data"][1]["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
completed_2 = datetime.strptime(order["data"][1]["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
difference_time_1 = (completed_2 - started_2).seconds
print(difference_time_1)

time = "%Y-%m-%dT%H:%M:%S.%fZ"
result = 0
for i in range(2):
    final_completed = datetime.strptime(order["data"][i]["startedAt"], time)
final_started = datetime.strptime(order["data"][i]["startedAt"], time)
result += (final_completed - final_started).seconds
assert result < 6, "время превышает 6 часов"
print("время равна ", result)
### 3-е задание:
