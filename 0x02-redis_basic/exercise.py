#!/usr/bin/python3
"""Function declares a redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counting how many times methods of the class Cache are called"""
    k = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapping the decorated func and returning the wrapper"""
        self.__redis.incr(k)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Storing the history of inputs and outputs for a particular func"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapping the decorated function and returning the wrapper"""
        key = method.__qualname__
        inp = str(args)
        self.__redis.rpush(key + ":inputs", inp)
        outp = str(method(self, *args, **kwargs))
        self.__redis.rpush(key + ":outputs", outp)
        return outp
    return wrapper


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