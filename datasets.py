from helpers import *


new_courier_credentials = {
    "login": "ninja3456t",
    "password": "1234b"
}

auth_credentials = {
    "login":"ninja3456t", 
    "password":"1234b"
}

not_exist_courier_credentials = {
    "login":"ninja3456tNoexist",
    "password":"1234bytf"
}

incorrect_auth_credentials = {
    "login":"ninja3456t", 
    "password":"1234b1234b"
}

empty_authorization_fields = [
{
    "login":"sambridges", 
    "password":""
},
{
    "login":"", 
    "password":"bridges"
}
]

empty_required_field = [
    {
    "login": '',
    "password": password,
    "firstName": first_name
    },
    {
    "login": login,
    "password": '',
    "firstName": first_name
    }
]

available_colors = [
    {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Moskovskii 115",
    "metroStation": 4,
    "phone": "+7 999 456 77 89",
    "rentTime": 3,
    "deliveryDate": "2025-11-11",
    "color": [
        "GREY"
    ]
},
    {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Moskovskii 115",
    "metroStation": 4,
    "phone": "+7 999 456 77 89",
    "rentTime": 3,
    "deliveryDate": "2025-11-11",
    "color": [
        "BLACK"
    ]
},
{
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Moskovskii 115",
    "metroStation": 5,
    "phone": "+7 999 456 77 89",
    "rentTime": 3,
    "deliveryDate": "2025-11-11",
    "color": [
        "BLACK",
        "GREY"
    ]
},
{
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Moskovskii 115",
    "metroStation": 5,
    "phone": "+7 999 456 77 89",
    "rentTime": 3,
    "deliveryDate": "2025-11-11",
    "color": [
    ]
}
]