#!/bin/bash

# update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# install nginx
sudo apt-get install nginx -y

# start nginx and enable
sudo systemctl start nginx
sudo systemctl enable nginx

#Install Node.js 6.x repositorynpm 
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install nodejs -y
sudo apt-get install npm #doesn't actually install npm
sudo npm install pm2 -g

#clone app from aws
git clone https://github.com/dav-par/eng114_app.git /home/ubuntu/app

#replace nginx default and run it
sudo rm -rf /etc/nginx/sites-available/default
sudo cp /home/ubuntu/app/default /etc/nginx/sites-available/
sudo systemctl restart nginx
sudo systemctl enable nginx

#set up the enviroment variable for DB_HOST
sudo echo "export DB_HOST=mongodb://34.241.254.31/posts" >> /home/ubuntu/.bashrc
source ~/.bashrc

cd app/app
sudo apt install npm
node seeds/seed.js
npm start