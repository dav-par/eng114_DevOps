#!/bin/bash

#update
sudo apt-get update -y

#upgrade
sudo apt-get upgrade -y

#install nginx
sudo apt-get install nginx -y

#start nginx
sudo systemctl start nginx

#enable nginx
sudo systemctl enable nginx

#get nodejs v6
sudo apt install curl
sudo curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install nodejs -y
sudo npm install pm2 -g
sudo apt-get install python-software-properties


cd app/app
npm install
npm start -d