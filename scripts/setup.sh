#!bin/bash

set -e 

apt-get update
apt-get install curl jq -y


if [ -z "$(docker --version 2> /dev/null)"]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $USER 
    newgrp docker
fi

if [ -z "$(docker-compose --version 2> /dev/null)"]; then
    version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi