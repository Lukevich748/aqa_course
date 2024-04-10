# 1
student = {
    "name": "Artem",
    "age": 29,
    "subjects": ["QA", "AQA"],
    "average_score": 8.3
}

average_score_update = student["average_score"] = 4.75
student["subjects"].append("Physics")
del student["age"]

assert "age" in student, "Key 'age' is not in dict 'student'"
assert "gender" in student, "Key 'gender' is not in dict 'student'"

print(student.keys())
print(student.values())

# 2
response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}

print(response["conditions"]["trustfactors"][0]["icon"])
print(response["conditions"]["campaign"]["id"])

assert response["conditions"]["trustfactors"][0]["helpIcon"] is False, "Value is not False"

type_value = response["services"][2]["type"]