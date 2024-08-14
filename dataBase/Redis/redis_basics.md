[Redis docs](https://redis.io/docs/latest/develop/get-started/)\
[redis crash course](https://www.youtube.com/watch?v=Hbt56gFj998)

1. redis in an open source in memory data structure store which can be use as database or a cache and message broker
2. NoSQL key/value store
3. supports multiple data structure
4. built in replication master/slave

### DataTypes
- strings
- lists
- sets
- sorted sets
- hashes
- bitmaps
- hyperlogs
- geospatial indexes

**redis is very flexable and very fast, No predetermined schemas or column names is needed, and can be used as a database, cache, streaming engine, message broker, and mor**

### installation
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install redis-server

**to start you shell interface**
`redis-cli`

**config file** is in /etc/redis/redis.conf

### getting started
**in your redis shell**\
`ping` it will respond with `pong` indicating established connectin
```
echo "something"
set name mostafa
get name
set age 21
incr age // will increment age to 22
decr age // decrement
exists name // check if a key exists
del name
flushall // will clear every thing you have set, it is like starting new session, all work you have done will be gone
type name //return the value type of the key
```

`quit` **to close connection**

### key space
**In Redis, a keyspace refers to the collection of all the keys stored in a particular database.**

- Redis can store many different keys, each associated with some value, like strings, lists, sets, etc.
- Redis supports multiple databases, each one holding its own set of keys.
- The keyspace is just a term for the entire set of keys within a specific Redis database.

##### key points
- Keyspace Notifications: Redis can notify you about certain events related to the keys (like when a key is created, updated, or deleted). This is known as keyspace notifications.
- Multiple Databases: Redis typically has multiple databases, and each one has its own separate keyspace.

So, when someone talks about the keyspace in Redis, they're simply referring to all the keys that exist in a particular Redis database.

```
set server:name someserver
set server: port 8000
get server: name
```
**the keyspace is server (the database) and it has two keys name and port**

### key expiration and persistence
**Key expiration lets you set a timeout for a key, also known as a "time to live", or "TTL". When the time to live elapses, the key is automatically destroyed.**

```
set greeting "hello"
expire greeting 10 // expires in 10 seconds
ttl greeting // will show the time lift
// if you want to set the expiration with the value at the same time
setx greeting 30 "hello" // expires in 30 sec
persist greeting // if you want to cancel the expiration while time still not out 
```
##### A few important notes about key expiration:

1. You can specify this expiration time in either seconds or milliseconds. For example, you could say, "This key should expire after 5 seconds" or "This key should expire after 5000 milliseconds" (which is the same as 5 seconds).
2. Precision of Expiration: Even though you can set the expiration time using either seconds or milliseconds, Redis always checks the expiration with millisecond precision. This means that Redis will track and enforce expirations down to the exact millisecond.
3. Expiration Information is Stored and Replicated: Redis not only keeps track of when each key should expire, but it also saves this information to disk. This is useful in case the server stops or restarts.
4. Persisting on Disk: When Redis saves data to disk, it also saves the exact time when each key is supposed to expire.
5. Time Passing Virtually: If your Redis server is turned off or crashes, the expiration times don’t pause. Redis remembers when the keys were supposed to expire, and when the server restarts, it checks if those keys should have already expired and removes them if needed.

**You can set keys in Redis to expire after a certain time using either seconds or milliseconds, but Redis always handles expiration with millisecond accuracy. Even if the server goes down, Redis remembers when each key was supposed to expire and removes them appropriately when it restarts.**

**For example using SET options:**\
`
set key 100 ex 10
OK
ttl key
(integer) 9
`

**The example above sets a key with the string value 100, having an expire of ten seconds. Later the TTL command is called in order to check the remaining time to live for the key.**

### navigating the key space
**To incrementally iterate over the keys in a Redis database in an efficient manner you can sue scan command, Another way to iterate over the keyspace is to use the KEYS command, but this approach should be used with care, since KEYS will block the Redis server until all keys are returned.**

### client side caching
[redis Ref](https://redis.io/docs/latest/develop/use/client-side-caching/)

**Client-side caching is a technique used to create high performance services. It exploits the memory available on application servers, servers that are usually distinct computers compared to the database nodes, to store some subset of the database information directly in the application side.**\
**Normally when data is required, the application servers ask the database about such information, like in the following diagram:**\
**When client-side caching is used, the application will store the reply of popular queries directly inside the application memory, so that it can reuse such replies later, without contacting the database again:**

#### The Redis client-side caching support is called Tracking, and has two modes:
- In the default mode, the server remembers what keys a given client accessed, and sends invalidation messages when the same keys are modified. This costs memory in the server side, but sends invalidation messages only for the set of keys that the client might have in memory.
- In the broadcasting mode, the server does not attempt to remember what keys a given client accessed, so this mode costs no memory at all in the server side. Instead clients subscribe to key prefixes such as object: or user:, and receive a notification message every time a key matching a subscribed prefix is touched.

### default mode
- Clients can enable tracking if they want. Connections start without tracking enabled.
- When tracking is enabled, the server remembers what keys each client requested during the connection lifetime (by sending read commands about such keys).
- When a key is modified by some client, or is evicted تم طرده because it has an associated expire time, or evicted because of a maxmemory policy, all the clients with tracking enabled that may have the key cached, are notified with an invalidation message.
- When clients receive invalidation messages, they are required to remove the corresponding keys, in order to avoid serving stale قديمه data.



#### connect
`redis-cli -h 127.0.0.1 -p 6379`