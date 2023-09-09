FROM debian:latest
RUN apt update && apt install -y python3 python3-pip python3-redis
#RUN pip3 install redis
COPY tls/ca-cert.pem /etc/ssl/redis-server-crt.pem
COPY tls/ca-key.pem /etc/ssl/redis-server-key.pem
COPY tls/ca-cert.pem /etc/ssl/ca-cert.pem
WORKDIR test
COPY redis_conn.py .
