FROM debian:latest

RUN apt-get update && apt-get install -y redis-server openssl

COPY redis.conf /etc/redis/redis.conf

COPY tls/ca-cert.pem /etc/ssl/redis-server-crt.pem
COPY tls/ca-key.pem /etc/ssl/redis-server-key.pem
COPY tls/ca-cert.pem /etc/ssl/ca-cert.pem

EXPOSE 6379
EXPOSE 6380

CMD ["redis-server", "/etc/redis/redis.conf"]
