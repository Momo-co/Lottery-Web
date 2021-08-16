#!/bin/bash

# Install dependencies
sudo apt update 
sudo apt install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible -y
sudo apt install ansible -y

ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml