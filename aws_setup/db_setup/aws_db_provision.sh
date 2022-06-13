#!/bin/bash

#get mongo_db keys
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927
echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list


#update and upgrade
sudo apt update -y
sudo apt upgrade -y


##install mongodb-org=3.2.20 -y
sudo apt install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20

##update the config file to open access
sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mongod.conf

##restart the database and enable it
sudo systemctl start mongod
sudo systemctl enable mongod

#mongo --eval 'db.runCommand({ connectionStatus: 1 })'