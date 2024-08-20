### Caching
- Imagine a library where books are stored on shelves. Retrieving a book from a shelf takes time, so a librarian decides to keep a small table near the entrance. This table is like a cache, where the librarian places the most popular or recently borrowed books.
![photo](https://media.geeksforgeeks.org/wp-content/uploads/20240110183740/Cache-Working.jpg)
- Caching is a common technique that aims to improve the performance and scalability of a system. It caches data by temporarily copying frequently accessed data to fast storage that's located close to the application.
- Caching helps applications perform dramatically faster and cost significantly less at scale
- Cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location.
- Caching allows you to efficiently reuse previously retrieved or computed data.
- The data in a cache is generally stored in fast access hardware such as RAM (Random-access memory) 
- Trading off capacity for speed, a cache typically stores a subset of data transiently, in contrast to databases whose data is usually complete and durable
- we don't recommend that you use the cache as the authoritative store of critical information. 
- The key to using a cache effectively lies in determining the most appropriate data to cache
- Caching typically works well with data that is immutable or that changes infrequently e: g reference information such as product and pricing information in an e-commerce application, or shared static resources that are costly to construct.
- Web clients typically use the URI of a resource as the key in the client-side cache, so if the URI changes, the web client ignores any previously cached versions of a resource and fetches the new version instead.
### Distributed Application Caching (2 ways)
- They use a private cache, where data is held locally on the computer that's running an instance of an application or service.
- They use a shared cache, serving as a common source that can be accessed by multiple processes and machines.
### client side and server side caching
- Client-side caching is done by the process that provides the user interface for a system, such as a web browser or desktop application.
- Server-side caching is done by the process that provides the business services that are running remotely.
### private caching
- The most basic type of cache is an in-memory store. It's held in the address space of a single process and accessed directly by the code that runs in that process
-  The size of a cache is typically constrained by the amount of memory available on the machine that hosts the process.
> [!NOTE]
> If you need to cache more information than is physically possible in memory, you can write cached data to the local file system. This process will be slower to access than data that's held in memory, but it should still be faster and more reliable than retrieving data across a network.
> If you have multiple instances of an application that uses this model running concurrently, each application instance has its own independent cache holding its own copy of the data.

> [!IMPORTANT]
> Think of a cache as a snapshot of the original data at some point in the past. If this data isn't static, it's likely that different application instances hold different versions of the data in their caches. Therefore, the same query performed by these instances can return different results
![photo](https://learn.microsoft.com/en-us/azure/architecture/best-practices/images/caching/figure1.png)
### shared caching
- If you use a shared cache, it can help alleviate concerns that data might differ in each cache, which can occur with in-memory caching. Shared caching ensures that different application instances see the same view of cached data. It locates the cache in a separate location, which is typically hosted as part of a separate service
![photo](https://learn.microsoft.com/en-us/azure/architecture/best-practices/images/caching/figure2.png)
- An important benefit of the shared caching approach is the scalability it provides. Many shared cache services are implemented by using a cluster of servers and use software to distribute the data across the cluster transparently. An application instance simply sends a request to the cache service. The underlying infrastructure determines the location of the cached data in the cluster. You can easily scale the cache by adding more servers.
> [!NOTE]
> in shared caching The cache is slower to access because it's no longer held locally to each application instance and The requirement to implement a separate cache service might add complexity to the solution.
### to know what data is best to cache
- carry out performance testing and usage analysis to determine whether prepopulating or on-demand loading of the cache, or a combination of both, is appropriate. The decision should be based on the volatility and usage pattern of the data. Cache utilization and performance analysis are important in applications that encounter heavy loads and must be highly scalable. For example, in highly scalable scenarios you can seed the cache to reduce the load on the data store at peak times.
### eviction policies
- it's possible that the cache might fill up if data is allowed to remain resident for a long time. In this case, any requests to add new items to the cache might cause some items to be forcibly removed in a process known as eviction. Cache services typically evict data on a least-recently-used (LRU) basis, but you can usually override this policy and prevent items from being evicted.

**There are several types of eviction policies. These include**
- A most-recently-used policy (in the expectation that the data won't be required again).
- A first-in-first-out policy (oldest data is evicted first).
- An explicit removal policy based on a triggered event (such as the data being modified).

### protect cached data
**2 main concerns here**
- The privacy of the data in the cache.
- The privacy of data as it flows between the cache and the application that's using the cache.

**implement an authentication mechanism that requires that applications specify the following:**
- Which identities can access data in the cache.
- Which operations (read and write) that these identities are allowed to perform.
### Ref
- [Microsoft] (https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching) \
still to read from "Considerations for implementing caching in Azure"
- [REf1](https://aws.amazon.com/ar/caching/)
- [GFG] (https://www.geeksforgeeks.org/caching-system-design-concept-for-beginners/)
