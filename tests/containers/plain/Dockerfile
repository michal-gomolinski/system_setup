FROM ubuntu:22.04

RUN apt update && \
  apt install -y \
    openssh-server \
    sudo

RUN useradd -m -s /bin/bash ansible && \
  adduser ansible sudo

ENTRYPOINT bash -c 'sleep infinity'

