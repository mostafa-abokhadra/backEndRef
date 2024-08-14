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
mset key1 "hello" key3 "world" // to set multiple key value pair
mget key1 key2 
append key1 " world" // appending string to key1 value
rename key1 greeting
lpush people "mostafa" // creating lists and adding mostafa, lpush (left push) so it push front
lrange people 0 -1 // list all items in people from first to last index
rpush people "ahmed" // push right (at the end)
llen people // length of list
lpop people // delete front
rpop people // delet end
linsert people before "mostafa" "newName" // insert middle
linsert people after "ahmed" "newName" // insert middle
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
hset user: "1" name: "mostafa-abokadra"
hset user: "1" email: "email@.com"
hgetall user: "1"

hmset user: "1" name "mostafa-abokhadra" email "email.com"
hkeys user: "1" // returns just the keys
hval user: "1" // returns just the values
hicerby user: "1" age 1 // increment user"1" age by 1
hdel user: "1" age
hlen user: "1"
```

### save
`save` create a snapshot of the data in the desk