#!/usr/bin/env python3
"""
"""
import requests
from typing import Dict

def send_req(user_name: str) -> Dict:
    if not isinstance(user_name, str):
        raise TypeError("user_name should be a string")
    url = f"https://api.github.com/users/{user_name}/repos"
    res = requests.get(url) # get function returns a response object
    return res.json() # json() convert json to python dictionary

def print_data(data: dict) -> None:
    if not isinstance(data, list):
        raise TypeError("data should be of type 'list'")
    for dicty in data:
        print(dicty["name"])
    return True