#!/usr/bin/env python3
"""
Module for LFU Caching policy
LFU means Least Frequently Used
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """Method that add key:value to the dictionary"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_key = self.keys_queue.pop(0)
                del self.cache_data[item_key]
                print("DISCARD:", item_key)
            self.cache_data[key] = item
            self.keys_queue.append(key)

    def get(self, key):
        """Method that return the value of the key"""
        if key in self.cache_data:
            self.keys_queue.remove(key)
            self.keys_queue.append(key)
            return self.cache_data[key]
        return None
