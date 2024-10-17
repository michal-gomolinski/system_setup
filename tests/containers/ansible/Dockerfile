FROM ubuntu:22.04

RUN apt update && \
  apt install -y \
    sudo \
    openssh-server \
    python3-pip && \
  python3 -m pip install --upgrade pip && \
  python3 -m pip install ansible && \
  service ssh start

RUN useradd -m -s /bin/bash ansible && \
  adduser ansible sudo && \
  echo "ansible ALL=(ALL:ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/ansible

USER ansible
ENTRYPOINT bash -c 'sleep infinity'

