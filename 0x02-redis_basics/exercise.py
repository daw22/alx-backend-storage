#!/usr/bin/env python3
"""
Redis - writing a string to redis
"""
import redis
import uuid
from typing import Union


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
