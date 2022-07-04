#!/bin/bash

cd app/app
node seeds/seed.js
npm start


#set up the enviroment variable for DB_HOST, souricng bashrc doesn't work
#So I ran the next two commands manually then made an ami
#sudo echo "export DB_HOST=mongodb://10.5.242.225:27017/posts" >> /home/ubuntu/.bashrc
#source /home/ubuntu/.bashrc ##doesn't work in 18.04 

#navigate to app folder, instal npm and run the app