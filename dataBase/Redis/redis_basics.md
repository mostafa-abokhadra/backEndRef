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

#### connect
`redis-cli -h 127.0.0.1 -p 6379`
```
SET bike:1 "Process 134"
GET bike:1
```
```
HSET bike:1 model Deimos brand Ergonom type 'Enduro bikes' price 4972
(integer) 4
HGET bike:1 model
"Deimos"
HGET bike:1 price
"4972"
HGETALL bike:1
1) "model"
2) "Deimos"
3) "brand"
4) "Ergonom"
5) "type"
6) "Enduro bikes"
7) "price"
8) "4972"
```

### keySpace
**Redis keys are binary safe; this means that you can use any binary sequence as a key, from a string like "foo" to the content of a JPEG file. The empty string is also a valid key.**

```
set mykey hello
type mykey //return the value type of the key
exists mykey //return true if key exists in the database
del mykey
```

### key expiration
**Before moving on, we should look at an important Redis feature that works regardless of the type of value you're storing: key expiration.**\
**Key expiration lets you set a timeout for a key, also known as a "time to live", or "TTL". When the time to live elapses, the key is automatically destroyed.**
##### A few important notes about key expiration:
- They can be set both using seconds or milliseconds precision.
- However the expire time resolution is always 1 millisecond.
- Information about expires are replicated and persisted on disk, the time virtually passes when your Redis server remains stopped (this means that Redis saves the date at which a key will expire).

```
set key some-value
expire key 5 # will expire after 5 second
get key # (immediately)
"some-value"
get key # (after 5 second)
(nil)
```

1. **The key vanished between the two GET calls, since the second call was delayed more than 5 seconds.**
2. **In the example above we used EXPIRE in order to set the expire (it can also be used in order to set a different expire to a key already having one, like PERSIST can be used in order to remove the expire and make the key persistent forever).**
3. **However we can also create keys with expires using other Redis commands.**

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



