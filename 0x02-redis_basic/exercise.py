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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))
