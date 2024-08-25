#!/usr/bin/env python3
"""getting repos of github user
"""
from functions import send_req
from functions import print_data

if __name__ == '__main__':
    res = send_req("mostafa-abokhadra")
    print_data(res)
