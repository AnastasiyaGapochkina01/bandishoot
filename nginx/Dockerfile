FROM debian:latest

RUN apt update && apt install -y ca-certificates curl procps iproute2 nginx
RUN apt-get autoremove --purge -y curl && \
    apt-get update && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists /var/cache/apt/archives

RUN rm /etc/nginx/sites-enabled/default

EXPOSE 8089

CMD ["nginx", "-g", "daemon off;"]
