#!/bin/bash

#update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

#install nginx
sudo apt-get install nginx -y

#start nginx and make sure it runs from boot
sudo systemctl start nginx
sudo systemctl enable nginx

#Install Node.js 6.x repositorynpm 
curl -sL https://deb.nodesource.com/setup_6.x | bash -

#set up the enviroment variable for DB_HOST
sudo echo "export DB_HOST=mongodb://192.168.10.150:27017/posts" >> /etc/bash.bashrc
source ~/.bashrc

#Install Node.js and npm
apt-get install -y nodejs
npm install pm2 -g

#copy over new default and run it
sudo rm -rf /etc/nginx/sites-available/default
sudo cp default /etc/nginx/sites-available/
sudo systemctl restart nginx
sudo systemctl enable nginx

#navigate to app folder, instal npm and run the app
cd app/app
#npm install
#npm start -d