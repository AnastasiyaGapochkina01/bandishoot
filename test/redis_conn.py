#!/usr/bin/python3

import redis

redis_client = redis.StrictRedis(
    host='172.21.0.3',
    port=6379,
    ssl=True,
    db=0,
    decode_responses=True,
    ssl_certfile='/etc/ssl/redis-server-crt.pem',
    ssl_keyfile='/etc/ssl/redis-server-key.pem',
    ssl_ca_certs='/etc/ssl/ca-cert.pem'
)

redis_client.set('my_key', 'my_value')


value = redis_client.get('my_key')

print("my_key: {}".format(value))
