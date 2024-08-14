#!/usr/bin/env python3
"""
Redis - writing a string to redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Inits Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data to redis and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, float, int]:
        """
        Get value from redis
        """
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """
        get a string value from redis
        """
        return self.get(key, lambda val: val.decode("utf8"))

    def get_int(self, key: str) -> int:
        """
        gets an Int value fro redis
        """
        return self.get(key, lambda val: int(val))
