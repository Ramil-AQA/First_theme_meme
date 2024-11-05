order  = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
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
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
    }
### Словарь; массивы, объекты
Operator = {
    'name' : 'Ramil',
    'mail' : 'ramilgrc2004@gmail.com'
}

ID_one = order["data"][0]["brand_id"]
ID_two = order["data"][1]["brand_id"]
ID_three = order["data"][2]["brand_id"]
mass = [ID_one, ID_two, ID_three]
print(mass)
Obj_dictionary = {
   'completed' : {
  'one' : order["data"][0]["completed"],
    'two' :   order["data"][1]["completed"],
       'three'  :   order["data"][2]["completed"]
},
    'wait_refund' : {
        'one': order["data"][0]["wait_refund"],
        'two': order["data"][1]["wait_refund"],
        'three': order["data"][2]["wait_refund"]
    },
    'refunded' :   {
        'one': order["data"][0]["refunded"],
        'two': order["data"][1]["refunded"],
        'three': order["data"][2]["refunded"]
}
}
print(Obj_dictionary)
### Конец словарика
if order == " " :
        print('status : ERROR')
else :
    print("status : OK")
result_time =  order["data"][0]["delay"] + order["data"][1]["delay"]
if result_time >= 6 :
    print("is not good <<<ERROR>>>")
else :
    print("status: OK")
if order == None :
    print ("is not good <<<ERROR>>>")
else :
    print("status: OK")
if len(order['data']) < 0 :
    print ("is not good <<<ERROR>>>")
else :
    print("status: OK")
Third_date1 = order["data"][2]["completed"]
Third_date2 = order["data"][2]["wait_refund"]
Third_date3 = order["data"][2]["refunded"]
if Third_date1 < order["data"][2]["count"] / 2 :
    print ("OK")
elif Third_date3 < Third_date1 :
    print ("OK")
elif  Third_date2  <= Third_date3 :
    print("OK")
else :
    print("ERROR")