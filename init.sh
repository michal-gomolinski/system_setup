#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y python3-pip

python3 -m pip install --upgrade pip


# Install uv
export UV_INSTALL_DIR="${HOME}/.local/bin"
curl -LsSf https://astral.sh/uv/install.sh | sh

${HOME}/.local/bin/uv tool run --from ansible ansible-playbook ./setup_playbook.yml
