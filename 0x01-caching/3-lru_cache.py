#!/usr/bin/env python3
"""
Module for LRU Caching plolicy
LRU means Least Recently Used
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """Method that add key:value to the dictionary"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.keys_queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.keys_queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Method that return the value of the key"""
        if key in self.cache_data:
            self.keys_queue.remove(key)
            self.keys_queue.append(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """Print the cache"""
        for key in self.keys_queue:
            print("{}: {}".format(key, self.cache_data[key]))
