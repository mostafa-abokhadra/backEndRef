### Cach Replacement Policy
- A cache replacement policy refers to the system's method of deciding <mark>which objects or content blocks should be removed from the cache when it becomes full</mark>. Factors such as the size of the object, the time of the last reference, the frequency of requests, the time of last modification, and the cost to fetch the object are all taken into consideration when designing a cache replacement policy. Various strategies, such as randomized, function-based, frequency-based, object size-based, and freshness-based, can be used to determine which objects are removed from the cache.
- the cache often has <mark>limited size</mark>. When the cache becomes full, some objects or content blocks must be removed to make room for new ones. A system has to take many factors into consideration for cache replacement. This is referred to as a <mark>cache replacement policy</mark>. 

### Factors to consider when designing the policy
- Size of the cached object
- Time of the last reference made to the cached object
- Frequency of the requests made to the object
- Time of last modification
- Cost to fetch the object from its original server

### least recently used
- A least recently used (LRU) cache replacement policy, where the least fresh object is removed, is a typical freshness-based mechanism ( the least recently used item is evicted to make room for new entries) (The order in which items are accessed. The most recently accessed items are retained, while the least recently accessed items are discarded when the cache is full.)

**Implementation Details:**
- Hash Map (Dictionary): Stores the key-value pairs for O(1) access.
- Doubly Linked List: Keeps track of the order of usage. The head represents the most recently used item, and the tail represents the least recently used item.
> [!NOTE]
> that mean you will have to use ordered dictionary to store the cach
```
from collection import orderedDict
cach = orderedDict()
```