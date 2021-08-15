#!bin/bash

set -e 

sudo apt-get update
sudo apt-get install curl jq -y
sudo apt install python3-venv
sudo apt install python3 -y
sudo apt install python3-pip

version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose