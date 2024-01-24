#!/usr/bin/python3
"""Function declares a redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    """Declaring a Cache class"""
    def __init__(self):
        """init to store an instance and flush"""
        self.__redis = redis.Redis(host='localhost', port=6379, db=0)
        self.__redis.flushdb()


def count_calls(method: Callable) -> Callable:
    """Counting how many times methods of the class Cache are called"""
    k = method.__qualname__