# pip install redis
# redis-py requires a running redis server

# to connect
import redis
r = redis.Redis(decode_responses=True) 
"""
    The decode_responses=True argument in redis.Redis() is used to automatically decode
    the data returned by Redis from bytes to strings.
    By default: When you interact with Redis using the redis-py library
    (which is the Python client for Redis), Redis returns data as raw bytes.
    Decoding: If you want the data returned by Redis (e.g., keys, values) to be
    automatically decoded to Python strings (using UTF-8 by default),
    you can set decode_responses=True.
"""
# or
r = redis.Redis(host="localhost", port="6379", db=0, password="", socket_timeout="" ,decode_responses=True)
"""
    The db parameter is the database number. You can manage multiple databases in Redis at once,
    and each is identified by an integer. The max number of databases is 16 by default.
"""
# or
r = redis.from_url('redis://host:port')
r.ping()

# set and get
r.set('mykey', 'myvalue') 
r.get('mykey').decode('utf-8') # if you haven't specified decode_response=True
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})