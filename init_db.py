#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymongo

initial_templates = [{"name": "typical form", "customer": "text", "customer_mail": "email", "customer_phone": "phone", "registered": "date"},
                     {"name": "admin contacts", "admin_mail": "email", "admin_phone": "phone"},
                     {"name": "order info", "order_date": "date", "details": "text"},
                     {"name": "mail list", "mailgroup": "text", "main_email": "email", "secondary_mail": "email", "emergency_mail": "email"},
                     {"name": "comments", "author": "text", "comment": "text"}
                     ]


def initialize_db():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    db = client["webforms"]
    templates = db["templates"]
    templates.insert_many(initial_templates)


if __name__ == "__main__":
    initialize_db()
