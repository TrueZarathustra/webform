#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import pymongo
import re


def is_date(string):
    # Possible formats:
    # DD.MM.YYYY
    # YYYY-MM-DD
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]

    for d in date_formats:
        try:
            datetime.datetime.strptime(string, d)
            return True
        except:
            pass
    return False


def is_phone(string):
    string = string.replace("-", "").replace(" ", "")
    return True if re.match(r'^7[\d]{10}$', string) else False


def is_email(string):
    return True if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', string) else False


def parameters_to_types(params):

    params_types = {}

    for k in params.keys():
        if is_date(params[k]):
            params_types[k] = "date"
        elif is_phone(params[k]):
            params_types[k] = "phone"
        elif is_email(params[k]):
            params_types[k] = "email"
        else:
            params_types[k] = "text"

    return params_types


def find_template(db_params, form):

    db_link = "mongodb://{host}:{port}/".format(**db_params)
    client = pymongo.MongoClient(db_link)
    db = client[db_params['db_name']]
    templates = db[db_params['collection']]

    for t in templates.find():
        if is_matched(form, t):
            return t['name']
    return None


def is_matched(form, template):

    for k in template.keys():
        if k not in ['_id', 'name']:
            if k not in form.keys():
                return False
            elif template[k] != form[k]:
                return False

    return True
