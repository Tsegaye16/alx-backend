#!/usr/bin/env python3
"""FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines:
    - caching system using FIFO algorithm
    """

    def __init__(self):
        """
        Initialize FIFOCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
