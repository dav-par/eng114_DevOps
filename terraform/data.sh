#!/bin/bash
#set up the enviroment variable for DB_HOST
sudo echo "export DB_HOST=mongodb://10.5.242.225:27017/posts" >> /home/ubuntu/.bashrc
sudo source /home/ubuntu/.bashrc

#navigate to app folder, instal npm and run the app
cd app/app
node seeds/seed.js
npm start