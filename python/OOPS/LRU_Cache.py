# LRU stands for "Least Recently Used," and an LRU Cache is a data structure that maintains a limited number of items,
# typically in the form of key-value pairs, and automatically evicts the least recently used item when the cache reaches its capacity. 
# The primary goal of an LRU Cache is to provide quick access to the most recently accessed items while efficiently managing the cache size.

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # A dictionary to store key-value pairs
        self.order = []  # A doubly-linked list to track the order of access

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1  # Return -1 for cache misses

    def put(self, key, value):
        if key in self.cache:
            # If the key already exists, update its value and move it to the end
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            # If the cache is at capacity, remove the least recently used item
            if len(self.cache) >= self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            # Add the new key-value pair to the cache and the end of the order list
            self.cache[key] = value
            self.order.append(key)

# Example usage:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1

cache.put(3, 3)  # Cache is at capacity, so it removes the least recently used item (2, 2)
print(cache.get(2))  # Output: -1 (2 is no longer in the cache)

cache.put(4, 4)  # Cache is still at capacity, so it removes the least recently used item (1, 1)
print(cache.get(1))  # Output: -1 (1 is no longer in the cache)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
print(cache)