# Redis
-  stands for Remote Dictionary Server.
- redis in an open source in memory data structure store which can be use as database or a cache and message broker
- NoSQL key/value store
- supports multiple data structure
- built in replication master/slave

### Keys and values

Every data object that you store in a Redis database has its own unique key. The key is a string that you pass to Redis commands to retrieve the corresponding object or modify its data. The data object associated with a particular key is known as the value and the two together are known as as key-value pair.

### Content of keys 
A key is typically a textual name that has some meaning within your data model. Unlike variable names in a programming language, Redis keys have few restrictions on their format, so keys with whitespace or punctuation characters are mostly fine (for example, "1st Attempt", or "% of price in $").

Redis doesn't support namespaces or other categories for keys, so you must take care to avoid name collisions. However, there is a **convention for using the colon** ":" character to split keys into sections (for example, "person:1", "person:2", "office:London", "office:NewYork:1"). You can use this as a simple way to collect keys together into categories.

Although keys are usually textual, Redis actually implements binary-safe keys, so you can use any sequence of bytes as a valid key, such as a JPEG file or a struct value from your app. The empty string is also a valid key in Redis.


> **redis is very flexable and very fast, No predetermined schemas or column names is needed, and can be used as a database, cache, streaming engine, message broker, and more**

## installation
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
```
**to start you shell interface**
```bash
redis-cli
```
it is to connect to a Redis server that runs on localhost (-h 127.0.0.1) and listens on the default port (-p 6379):
```bash
redis-cli -h 127.0.0.1 -p 6379
```

**config file** is in <mark>/etc/redis/redis.conf</mark>

### getting started
**in your redis shell**\
`ping` it will respond with `pong` indicating established connectin

Similar to byte arrays, Redis strings store sequences of bytes, including text, serialized objects, counter values, and binary arrays

### Basics
```bash
> echo "something"
> set name mostafa
> get name
> set age 21
> incr age // will increment age to 22 adn saved in age like ++age
> decr age // decrement
> exists name // check if a key exists
> del name
> flushall // will clear every thing you have set, it is like starting new session, all work you have done will be gone
> type name //return the value type of the key
> mset key1 "hello" key3 "world" // to set multiple key value pair
> mget key1 key2 
> append key1 " world" // appending string to key1 value
> rename key1 greeting
> lpush people "mostafa" // creating lists and adding mostafa, lpush (left push) so it push front
> lrange people 0 -1 // list all items in people from first to last index
> rpush people "ahmed" // push right (at the end)
> llen people // length of list
> lpop people // delete front
> rpop people // delet end
> linsert people before "mostafa" "newName" // insert middle
> linsert people after "ahmed" "newName" // insert middle
```
`quit` **to close connection**

### Redis Datatypes
1. Json: differs from Hash, read [this](https://redis.io/docs/latest/develop/data-types/json/)
2. read about other datatypes in detail [here](https://redis.io/docs/latest/develop/data-types/)

### Key expiration 
Key expiration lets you set a timeout for a key, also known as a "time to live", or "TTL". When the time to live elapses, the key is automatically destroyed.

- They can be set both using seconds or milliseconds precision.
- However the expire time resolution is always 1 millisecond.
- Information about expires are replicated and persisted on disk, the time virtually passes when your Redis server remains stopped (this means that Redis saves the date at which a key will expire).


read [this](https://redis.io/docs/latest/develop/using-commands/keyspace/)

### key space

Each item within Redis has a unique key. All items live within the Redis keyspace. You can scan the Redis keyspace via the SCAN command.
```bash
scan 0 # would show all keys set
scan 0 match "name:*" count 40 # would show 40 keys that match specific match
```
SCAN returns a cursor position, allowing you to scan iteratively for the next batch of keys until you reach the cursor value 0.

**In Redis, a keyspace refers to the collection of all the keys stored in a particular database.**

- Redis can store many different keys, each associated with some value, like strings, lists, sets, etc.
- Redis supports multiple databases, each one holding its own set of keys.
- The keyspace is just a term for the entire set of keys within a specific Redis database.

##### key points
- **Keyspace Notifications**: Redis can notify you about certain events related to the keys (like when a key is created, updated, or deleted). This is known as keyspace notifications.
- **Multiple Databases**: Redis typically has multiple databases, and each one has its own separate keyspace.

So, when someone talks about the keyspace in Redis, they're simply referring to all the keys that exist in a particular Redis database.

#### key expiration and persistence
**Key expiration lets you set a timeout for a key, also known as a "time to live", or "TTL". When the time to live elapses, the key is automatically destroyed.**

```bash
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

### set
```
saad cars "ford" // adding to the set
saad cars "honda"
saad cars "bmw"
sismemeber cars "honda" // returns true if honda is memebre of cars set
smembers cars // returns all members
scard cars // number of elements (lenght)
smove cars to newSet "ford" // moving one set member to another set
srem cars "bmw" // removing item from cars
```

### sorted sets
```
// 
zadd users 1980 "name1" // adding to sortedset called users
zadd users 1985 "name2" // you add a score and the value
zadd users 1982 "name3" // the sorted set will be sorted acc. to score
zadd users 1984 "name4"
zadd users 1981 "name5"
zrange users 0 -1
zincrby users 12 "name3" // this will increment 12 to the score of "name3" 
```

### hash
```
hset user:"1" name: "mostafa-abokadra"
hset user:"1" email: "email@.com"
hgetall user:"1"

hmset user:"1" name "mostafa-abokhadra" email "email.com"
hkeys user:"1" // returns just the keys
hval user:"1" // returns just the values
hicerby user:"1" age 1 // increment user"1" age by 1
hdel user:"1" age
hlen user:"1"
```
### save
`save` create a snapshot of the data in the desk

# Ref
[Redis docs](https://redis.io/docs/latest/develop/get-started/)\
[redis crash course](https://www.youtube.com/watch?v=Hbt56gFj998)
