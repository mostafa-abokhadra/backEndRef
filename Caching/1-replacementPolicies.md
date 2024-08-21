### Cach Replacement Policy
- A cache replacement policy refers to the system's method of deciding <mark>which objects or content blocks should be removed from the cache when it becomes full</mark>. Factors such as the size of the object, the time of the last reference, the frequency of requests, the time of last modification, and the cost to fetch the object are all taken into consideration when designing a cache replacement policy.
- the cache often has <mark>limited size</mark>. When the cache becomes full, some objects or content blocks must be removed to make room for new ones. A system has to take many factors into consideration for cache replacement. This is referred to as a <mark>cache replacement policy</mark>. 

### Factors to consider when designing the policy
- Size of the cached object
- Time of the last reference made to the cached object
- Frequency of the requests made to the object
- Time of last modification
- Cost to fetch the object from its original server

```python
#!/usr/bin/python3
""" BaseCaching module
"""
class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))
    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")
    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

1. ### FIFO
- the first data entered into the cache is the first to be removed when the cache reaches its limit. This approach is straightforward and ensures that the oldest data is removed first.
```python
class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            deleted = list(self.cache_data.keys())[0]
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")
```

2. ### LIFO
- the most recently added data is the first to be removed when the cache reaches its limit. This approach is less common in caching but is used in certain scenarios where the most recent data is likely to be the least needed.
```python
BaseCaching = __import__('base_caching').BaseCaching
class LIFOCache(BaseCaching):
    last_modified = ''
    def __init__(self):
        super().__init__()
    def put(self, key, item):
        last_modified = ''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) == super().MAX_ITEMS:
            LIFOCache.last_modified = key
        if len(self.cache_data) > super().MAX_ITEMS:
            del self.cache_data[LIFOCache.last_modified]
            print(f"DISCARD: {LIFOCache.last_modified}")
            LIFOCache.last_modified = key
    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
```
3. ### least recently used
- the least recently accessed data is removed first when the cache reaches its limit. This approach is based on the principle that data accessed least recently is less likely to be needed in the future.

**Implementation Details:**
- Hash Map (Dictionary): Stores the key-value pairs for O(1) access.
- Doubly Linked List: Keeps track of the order of usage. The head represents the most recently used item, and the tail represents the least recently used item.
> [!NOTE]
> that mean you will have to use ordered dictionary to store the cach
```
from collection import orderedDict
cach = orderedDict()
```
4. ### Most Recently used
- the most recently accessed data is removed first when the cache reaches its limit. This is the opposite of the Least Recently Used (LRU) strategy. The idea behind MRU is that in some scenarios, the most recently used items are less likely to be accessed again compared to older items.

5. ### least frequently accessed
- A least frequently accessed (LFA) policy looks at the frequency of the objects being requested to determine the order of removal. That is, those objects that are being accessed frequently will be kept, whereas those that are not will be considered for deletion first. 
- Tie-breaking: When multiple items have the same frequency, additional criteria, such as recency (using LRU as a secondary strategy), can be used to determine which item to evictor the oldest one (based on insertion order) is removed.

6. ### minimum size and maximum size policy
- A minimum size (MinS) cache replacement policy takes object size into consideration. The smallest object is removed first. Opposite MinS is another straightforward object size-based strategy, namely a 
maximum size policy (MaxS) whereby the largest object is considered for elimination first.
