### Caching
- Caching is a common technique that aims to improve the performance and scalability of a system. It caches data by temporarily copying frequently accessed data to fast storage that's located close to the application.
- Caching helps applications perform dramatically faster and cost significantly less at scale
- Cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location.
- Caching allows you to efficiently reuse previously retrieved or computed data.
- The data in a cache is generally stored in fast access hardware such as RAM (Random-access memory) 
- Trading off capacity for speed, a cache typically stores a subset of data transiently, in contrast to databases whose data is usually complete and durable
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

### Ref
- [REf1](https://aws.amazon.com/ar/caching/)
