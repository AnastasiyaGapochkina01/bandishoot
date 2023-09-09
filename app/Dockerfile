FROM debian:latest

RUN apt update -y && apt install -y wget procps iproute2 curl ca-certificates vim
RUN apt-get autoremove --purge -y curl && \
    apt-get update && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists /var/cache/apt/archives

WORKDIR /go
RUN wget https://golang.org/dl/go1.20.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.20.2.linux-amd64.tar.gz
RUN cp /usr/local/go/bin/go /usr/local/bin
COPY code/ .
EXPOSE 8080

CMD ["go","run","main.go"] 

#RUN echo "export PATH=/usr/local/go/bin:${PATH}" | tee -a $HOME/.profile
#RUN /bin/bash -ic "source ~/.profile"

