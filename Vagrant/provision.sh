#!/bin/bash

#update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

#install nginx
sudo apt-get install nginx -y

#start nginx and make sure it runs from boot
sudo systemctl start nginx
sudo systemctl enable nginx

# Install Node.js 6.x repository
curl -sL https://deb.nodesource.com/setup_6.x | bash -

# Install Node.js and npm
apt-get install -y nodejs
npm install pm2 -g

#navigate to app folder, instal npm and run the app
cd app/app
npm install
npm start -d