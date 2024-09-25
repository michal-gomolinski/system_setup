This repository contains opinionated automatic personal setup of a linux machine

## OS Distro: Ubuntu 22.04 (Jammy)

- Possible upgrade to Ubuntu 24.04
- Possible switch to another Linux Distro

## Required tooling

### Python

Ubuntu 22.04 comes with Python 3.10 installed that may be
recent enough, however some packages still need to be installed

```bash
sudo apt-get install python3-pip
sudo apt-get install python3-venv
```

### Ansible

Ansible is needed for the automatic configuration process itself

```bash
pip install ansible
```

### Docker

Add apt repositories

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Reference:
<https://docs.docker.com/engine/install/ubuntu/>

### Neovim

Neovim in official apt repositories is outdated, install it from prebuilt binaries

```bash
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
sudo rm -rf /opt/nvim
sudo tar -C /opt -xzf nvim-linux64.tar.gz
```

Add the following to your .zshrc or .bashrc

```bash
export PATH="$PATH:/opt/nvim-linux64/bin"
```

### Zsh

Installing with apt

```bash
sudo apt-get install zsh
```

Warning: The version of Zsh in the official repositories is outdated

#### Plugins

- git
- zsh-autosuggestions
- zsh-z
- copilot

### Kubectl

```bash
# Download latest binary
curl -LO "https://dl.k8s.io/release/$(curl -L -s \ 
https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" 
# Download checksum file
curl -LO "https://dl.k8s.io/release/$(curl -L -s \
https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
# Verify downloaded binaries
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
# Install kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# Verify installation
kubectl version --client
```

#### Kubectx

#### Kubens

## Optional

### Nodejs

Install Node Version Manager

<https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating>

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm-sh

nvm install v20.17.0
```

Make sure to the export from above to be in your .zshrc or .bashrc
