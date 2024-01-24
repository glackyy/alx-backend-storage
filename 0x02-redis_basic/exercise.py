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
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """taking a data arg and returning a string"""
        rk = str(uuid4())
        self.__redis.set(rk, data)
        return rk

    def get(self, key: str, 
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Converting the data back to the desired format"""
        val = self.__redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """Parametrizing Cache get with the correct conversion func"""
        val = self.__redis(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametrizing Cache get with the correct conversion func"""
        val = self.__redis(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
def count_calls(method: Callable) -> Callable:
    """Counting how many times methods of the class Cache are called"""
    k = method.__qualname__