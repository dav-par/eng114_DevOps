#!/bin/bash

# update and upgrade
sudo apt update -y && sudo apt upgrade -y
sudo apt-get update -y

#install ansible	
sudo apt-get install software-properties-common
	
sudo apt-add-repository ppa:ansible/ansible -y
	
sudo apt-get update
	
sudo apt-get install ansible -y

git clone https://github.com/dav-par/working_ansible.git /etc/ansible