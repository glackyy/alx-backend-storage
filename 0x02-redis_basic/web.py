#!/usr/bin/env python3
"""Web Caching and tracker"""
import requests
import redis
from functools import wraps


store = redis.Redis()


def ct_url_access(method):
    """Decorator counting times a url is accessed"""
    @wraps(method)
    def wrapper(url):
        c_key = "cached:" + url
        c_data = store.get(c_key)
        if c_data:
            return c_data.decode("utf-8")
