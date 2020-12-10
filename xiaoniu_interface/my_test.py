# coding=utf-8
import requests
import json
from flask import Flask, jsonify


def my_login(user, password):
    url = 'http://127.0.0.1:5000/login'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"user": user, "password": password}
    re = requests.post(url=url, data=data, headers=headers)
    # print(re.status_code, json.loads(re.text))

    return [re.status_code]



