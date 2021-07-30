#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests


def test_case_to_string(tc):
    output = ""
    for k in tc.keys():
        output += "{param}={value}&".format(param=k, value=tc[k])
    return output[:-1]


app_config = {"host": "127.0.0.1",
              "port": 5000,
              "log_level": "info"}


test_cases = [{"customer": "Max", "customer_mail": "max@maxmail.ru", "customer_phone": "+79991112233", "registered": "12.07.2018"},
              {"admin_mail": "admin@admin.pro", "admin_phone": "+71234567890"},
              {"order_date": "2020-10-10", "details": "Order num 1233. Very important!"},
              {"mailgroup": "mymails", "main_email": "me@memail.com", "secondary_mail": "metoo@memail.com", "emergency_mail": "em@memail.com"},
              {"author": "Cool Author", "comment": "the good one"},
              {"Last date": "2010-03-23", "comment": "some text"},
              {"admin_mail": "admin@admin.pro", "admin_phone": "CALLME"}
              ]

print("\n\nStart testing. Expect to find only first 5 templates")
for tc in test_cases:
    params = test_case_to_string(tc)
    print("\nCheck case: ", params)
    url = 'http://{host}:{port}/get_form?{params}'.format(params=params, **app_config)
    r = requests.post(url)
    print("Output: ", r.text)
