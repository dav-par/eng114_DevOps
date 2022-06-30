#!/bin/bash

# update and upgrade
sudo apt update -y && sudo apt upgrade -y
sudo apt-get update -y

#install ansible	
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get update
sudo apt-get install ansible -y

#install python and boto3
sudo apt install python
sudo apt install python-pip -y
sudo pip install --upgrade pip
sudo pip install boto
sudo pip install boto3

sudo rm -rf /etc/ansible
sudo git clone -b vagrant https://github.com/dav-par/working_ansible.git /etc/ansible
export ANSIBLE_HOST_KEY_CHECKING=False

cd /etc/ansible
sudo mkdir group_vars
cd group_vars
sudo mkdir all

#cd /etc/ansible
#ansible-playbook 1_nginx.yml
#ansible-playbook 2_proxy.yml
#ansible-playbook 3_nodejs.yml
#ansible-playbook 4_mongo.yml
#ansible-playbook 5_copy_app.yml