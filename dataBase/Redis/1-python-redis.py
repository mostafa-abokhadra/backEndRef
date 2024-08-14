# pip install redis
# redis-py requires a running redis server

# to connect
import redis
r = redis.Redis()
# or
r = redis.Redis(host="", port="")
# or
r = redis.from_url('redis://host:port')
r.ping()