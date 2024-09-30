FROM ubuntu:22.04

RUN apt update && \
  apt install -y openssh-server \
    sudo

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN useradd -m -s /bin/bash sshuser && \
  echo "sshuser:sshuser" | chpasswd && \
  adduser sshuser sudo

EXPOSE 22

ENTRYPOINT service ssh start && bash -c 'sleep infinity'

