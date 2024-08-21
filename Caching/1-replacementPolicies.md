### Cach Replacement Policy
- A cache replacement policy refers to the system's method of deciding <mark>which objects or content blocks should be removed from the cache when it becomes full</mark>. Factors such as the size of the object, the time of the last reference, the frequency of requests, the time of last modification, and the cost to fetch the object are all taken into consideration when designing a cache replacement policy.
- the cache often has <mark>limited size</mark>. When the cache becomes full, some objects or content blocks must be removed to make room for new ones. A system has to take many factors into consideration for cache replacement. This is referred to as a <mark>cache replacement policy</mark>. 

### Factors to consider when designing the policy
- Size of the cached object
- Time of the last reference made to the cached object
- Frequency of the requests made to the object
- Time of last modification
- Cost to fetch the object from its original server

1. ### FIFO
- the first data entered into the cache is the first to be removed when the cache reaches its limit. This approach is straightforward and ensures that the oldest data is removed first.

2. ### LIFO
- the most recently added data is the first to be removed when the cache reaches its limit. This approach is less common in caching but is used in certain scenarios where the most recent data is likely to be the least needed.

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

### least frequently accessed
- A least frequently accessed (LFA) policy looks at the frequency of the objects being requested to determine the order of removal. That is, those objects that are being accessed frequently will be kept, whereas those that are not will be considered for deletion first. 
- Tie-breaking: When multiple items have the same frequency, additional criteria, such as recency (using LRU as a secondary strategy), can be used to determine which item to evictor the oldest one (based on insertion order) is removed.

### Most Recently used
- Most Recently Used (MRU) is a caching strategy that evicts the most recently accessed item first when the cache reaches its capacity. This is the opposite of the Least Recently Used (LRU) strategy. The idea behind MRU is that in some scenarios, the most recently used items are less likely to be accessed again compared to older items.

### minimum size and maximum size policy
- A minimum size (MinS) cache replacement policy takes object size into consideration. The smallest object is removed first. Opposite MinS is another straightforward object size-based strategy, namely a 
maximum size policy (MaxS) whereby the largest object is considered for elimination first.