#!/usr/bin/env python3
import redis
import uuid
from typing import Union
"""
Task 0: Writing strings to Redis
"""

class Cache:
    """ Create class Cache """
    def __init__(self):
        """ Initialize class """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """ Stored data in redis instance """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
