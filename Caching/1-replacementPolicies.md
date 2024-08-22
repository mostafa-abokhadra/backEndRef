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
- the code implementation is not exactly last in first out, it's last modified first out
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
```python
class LRUCache(BaseCaching):
    least_used = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ the logic is as follow:
                - what ever operation (put, get, updata) happens on our self.cache_data
                we will log these to into the least_used list
                - the last item in the least will always be the least used to be removed whenever 
                cache reach it's maximum limits
                - if size of cache_data before and after put operation is the same that indicate an update operation not appending or adding new value which has it's own logic
                - if size of cache_data after put operatoin is bigger than before that indicates
                adding new value which has it's own logic
                - whenever we "get", or "put" any item we will add this item to the front of the least_used list meaning that this item is recently used so not to be considered when removal time comes, this will also make the last item of the least_used list always the least recently used which we pop from the list when time comes and from the cache_data
        """
        if key is None or item is None:
            return
        copy = self.cache_data.copy()
        self.cache_data[key] = item
        if len(copy) == len(self.cache_data): 
            if not LRUCache.least_used:
                LRUCache.least_used.append(key)
            else:
                idx = LRUCache.least_used.index(key)
                key = LRUCache.least_used[idx]

                del LRUCache.least_used[idx]
                LRUCache.least_used.insert(0, key)
        else:
            LRUCache.least_used.insert(0, key)

        if len(self.cache_data) > super().MAX_ITEMS:
            deleted = LRUCache.least_used.pop()
            print(f"DISCARD: {deleted}")
            del self.cache_data[deleted]

    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        idx = LRUCache.least_used.index(key)
        key = LRUCache.least_used[idx]
        del LRUCache.least_used[idx]
        LRUCache.least_used.insert(0, key)
        return self.cache_data[key]
```

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
- the most recently accessed data is removed first when the cache reaches its limit. This is the opposite of the Least Recently Used (least_used) strategy. The idea behind MRU is that in some scenarios, the most recently used items are less likely to be accessed again compared to older items.
```python
class MRUCache(BaseCaching):
    """ the logic is as follow:
        literally the same as the least recently used
        but instead of poping out the last item from the
        lru list indicating the least recently used, we
        just poping out the first element of the list
        indicating most recently used, note that we don't
        pop list[0] but we pop out list[1] that is because we
        add the new item to the cache at the beginning of the
        self.cache_data before we actually empty the space
        so the item that need to be deleted moves from first
        postion to the second postion "list[1]"
    """
    mru = []
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        copy = self.cache_data.copy()
        self.cache_data[key] = item
        if len(copy) == len(self.cache_data):
            if not MRUCache.mru:
                MRUCache.mru.append(key)
            else:
                idx = MRUCache.mru.index(key)
                key = MRUCache.mru[idx]
                del MRUCache.mru[idx]
                MRUCache.mru.insert(0, key)
        else:
            MRUCache.mru.insert(0, key)
        if len(self.cache_data) > super().MAX_ITEMS:
            deleted = MRUCache.mru[1]
            print(f"DISCARD: {deleted}")
            del self.cache_data[deleted]
            del MRUCache.mru[1]

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        idx = MRUCache.mru.index(key)
        key = MRUCache.mru[idx]
        del MRUCache.mru[idx]
        MRUCache.mru.insert(0, key)
        return self.cache_data[key]
```
5. ### least frequently accessed
- A least frequently accessed (LFA) policy looks at the frequency of the objects being requested to determine the order of removal. That is, those objects that are being accessed frequently will be kept, whereas those that are not will be considered for deletion first. 
- Tie-breaking: When multiple items have the same frequency, additional criteria, such as recency (using least_used as a secondary strategy), can be used to determine which item to evictor the oldest one (based on insertion order) is removed.
```python
class LFUCache(BaseCaching):
    """ the logic is as follow:
        - when we first put or add into cahce_data, we will put
        the same element key in the lfu_lru dictionary with the 
        value of 1 (indicating only one operation have been
        done on that key which is the addition operation till now)
        -whenever that key is used again either by
        put function(updating it's value) or by get function
        we will increment it's value by +1 and at the same time
        we will move it at the beginning of the dictionary indicating
        the most recently used
        - when we reach the limits, we will loop on the values of
        lfu_lru dictionary and find the minimum value which indicates
        the least frequently used, then we will count how many times this
        minumum number is repeated as another keys value, if it exists only
        once then we will just remove this item, if it is repeated
        more than one time as multiple keys value we will remove the item
        according to the recency by looping on the dictionary from the end
        and find the first occurance of the minimum value from the end which
        indicates the least recently used
        (lastkeys in the dictionary is the older keys)
        -Note that when we tried to find the minimum value of dict.values()
        we started from index 1, because index 0 is for the new item which 
        is just added right now so it's counter gonna be 1, so exclude that
    """
    lfu_lru = {}
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        copy = self.cache_data.copy()
        self.cache_data[key] = item
        if len(copy) == len(self.cache_data):
            LFUCache.lfu_lru[key] = LFUCache.lfu_lru[key] + 1
            new_dict = dict({key: LFUCache.lfu_lru[key]})
            del LFUCache.lfu_lru[key]
            LFUCache.lfu_lru = {**new_dict, **LFUCache.lfu_lru}
        else:
            LFUCache.lfu_lru = {**{key: 1}, **LFUCache.lfu_lru}
        if len(self.cache_data) > super().MAX_ITEMS:
            deleted = ""
            leastFrequent = min(list(LFUCache.lfu_lru.values())[1:])
            checkSimilarFrequencey = list(
                LFUCache.lfu_lru.values()).count(leastFrequent)
            if checkSimilarFrequencey == 1:
                for key in LFUCache.lfu_lru.keys():
                    if LFUCache.lfu_lru[key] == leastFrequent:
                        deleted = key
                        del LFUCache.lfu_lru[key]
                        del self.cache_data[key]
                        break
            else:
                for k, v in reversed(LFUCache.lfu_lru.items()):
                    if v == leastFrequent:
                        deleted = k
                        del self.cache_data[k]
                        del LFUCache.lfu_lru[k]
                        break
            print(f"DISCARD: {deleted}")
    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        LFUCache.lfu_lru[key] += 1
        new_dict = dict({key: LFUCache.lfu_lru[key]})
        del LFUCache.lfu_lru[key]
        LFUCache.lfu_lru = {**new_dict, **LFUCache.lfu_lru}
        return self.cache_data[key]
```

6. ### minimum size and maximum size policy
- A minimum size (MinS) cache replacement policy takes object size into consideration. The smallest object is removed first. Opposite MinS is another straightforward object size-based strategy, namely a 
maximum size policy (MaxS) whereby the largest object is considered for elimination first.
