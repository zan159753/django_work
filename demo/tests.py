import redis as redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
print(r.ping())