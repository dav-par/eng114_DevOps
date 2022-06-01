# Vagrantup
https://www.vagrantup.com/intro

Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.

![Vagrant diagram](/Documentation/resources/vagrant.png)

## Common commands
- `vagrant init` - intialise first install of a box
- `vagrant reload` - reloads the config file whilst keeping the system up
- `vagrant destroy` - destroys the vm in your directory
- `vagrant halt` - stop the machine
- `vagrant up` - load file
- `vagrant ssh` - ssh in


## Set up your provisions file
A provision file is a bash script that you can call when setting up a vm using vagrant


## Linux commands you can do in a provisions file
- `sudo apt-get update` update system
- `sudo apt-get upgrade` upgrade system
- `sudo apt-get install nginx -y` - install nginx
- open `192.168.10.100` in browser to test it
- `sudo ./provision.sh`


## Building a vagrant config file
- first choose your box - https://app.vagrantup.com/boxes/search 
- configure the features you need:
    - `config.vm.network "private_network", ip: "192.168.10.100"` - sets up a network on the ip listed
- `config.vm.provision "file", source: "./provision.sh", destination: "$HOME/"` copies a `file` from the source to the detination. `$HOME/` is the variable for the home directory
- `config.vm.provision "shell", inline: "sudo chmod +x provision.sh && sudo ./provision.sh", run:"always"` runs a shell inline and gives `provision.sh` the permission to execute and(&&) runs it as sudo


## Deploying an app to a new machine
- Talk to the devs and find out the requirments and dependences
    - where does it need to be deployed too?
    - nodesjs
    - how many users can it handle?
    - does it need to be automated?
    - what is the time frame?
    - what type of requests?
    - what are the dependecies required?
    - which language does it support?
- set up the above vagrant file
- test your dependendences
- write script to run all the installs
- if your app is all in one folder, move it to the same folder as the vagrantfile with this code in the vagrantfile:
    - `config.vm.synced_folder "./app", "/home/vagrant/app"`


## provision file for test app
------
`#!/bin/bash` MUST HAVE to start a script 

#update 
`sudo apt-get update -y` - updates the software of the vm and skips the yes/no prompt

#upgrade
`sudo apt-get upgrade -y` - upgrades too the newest version

#install nginx
`sudo apt-get install nginx -y` - installs nginx a web server

#start nginx
`sudo systemctl start nginx` - runs the webserver

#enable nginx
`sudo systemctl enable nginx` - tells the webserver that it should stay on always 

#get nodejs v6
`sudo apt install curl` - installs curl
`sudo curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -` -installs node vs6.x
 - [wiki on curl](https://en.wikipedia.org/wiki/CURL)
 - [curl command examples](https://www.tecmint.com/linux-curl-command-examples/)
 - [curl args](https://devhints.io/curl)
 - -s makes it silent -L makes it follow links
 - then the link 
 - `|` pipes the output from the first command in to end of the second at the - locations 
 - [Pipe tips](https://linuxhint.com/linux-pipe-command-examples/)



`sudo apt-get install nodejs -y`
`sudo npm install pm2 -g`
`sudo apt-get install python-software-properties`

`cd app/app`
`npm install`
`npm start -d`
------
## Set up the machine
- set up your vagrant file
- set your provisions file
- run vagrant up
