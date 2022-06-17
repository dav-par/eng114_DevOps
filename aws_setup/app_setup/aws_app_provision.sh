#!/bin/bash

# update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# install nginx
sudo apt-get install nginx -y

# start nginx and enable
sudo systemctl start nginx
sudo systemctl enable nginx

#Install dependencies 
sudo apt-get install nodejs -y
sudo apt install npm -y
npm install pm2 -g
npm install n -g && n stable

#clone app from github
git clone https://github.com/dav-par/eng114_app.git /home/ubuntu/app

#replace nginx default and run it
sudo rm -rf /etc/nginx/sites-available/default
sudo cp /home/ubuntu/app/default /etc/nginx/sites-available/
sudo systemctl restart nginx
sudo systemctl enable nginx

#set up the enviroment variable for DB_HOST
sudo echo "export DB_HOST=mongodb://10.0.75.149/posts" >> /home/ubuntu/.bashrc
source ~/.bashrc

cd /home/ubuntu/app/app && npm install
nohup node app.js > /dev/null 2>&1 &