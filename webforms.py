#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request
from helper_functions import find_template, parameters_to_types
import uvicorn

app_config = {"host": "127.0.0.1",
              "port": 5000,
              "log_level": "warning"}

db_config = {"host": "127.0.0.1",
             "port": 27017,
             "db_name": "webforms",
             "collection": "templates"}

app = FastAPI()

@app.post("/get_form")
def get_form(request: Request):
    params = request.query_params
    form = parameters_to_types(params)
    template = find_template(db_config, form)
    if template:
        return template
    else:
        return form

if __name__ == "__main__":
    uvicorn.run(app, **app_config)
