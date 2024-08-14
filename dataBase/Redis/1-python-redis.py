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
r = redis.Redis(host="", port="", decode_responses=True)
# or
r = redis.from_url('redis://host:port')
r.ping()