[link to index](/readme.md)  
# Vagrant
https://www.vagrantup.com/intro
Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.

![Vagrant diagram](/Documentation/resources/vagrant.png)

## Common commands
`vagrant init` - intialise first install of a box  
`vagrant reload` - reloads the config file whilst keeping the system up  
`vagrant destroy` - destroys the vm in your directory  
`vagrant halt` - stop the machine  
`vagrant up` - load file  
`vagrant ssh` - ssh in  

## Set up your provisions file
A provision file is a bash script that you can call when setting up a vm using vagrant  
Use `nano provision.sh` to make it in nano  
Don't use notepad or windows files, it wont copy over properly, make sure to open with `#!/bin/bash`

## If your vagrant file breaks
- delete the .vagrant folder
- use vm virtualbox manager to power off and remove the machine

## Linux commands you can do in a provisions file
- `sudo apt-get update` update system
- `sudo apt-get upgrade` upgrade system
- `sudo apt-get install nginx -y` - install nginx
- open `192.168.10.100` in browser to test it
- `sudo ./provision.sh`

## Building a vagrant config file
- first choose your box - https://app.vagrantup.com/boxes/search 
- configure the features you need:
    - `config.vm.network "private_network", ip: "192.168.10.100"`
        - sets up a network on the ip listed
    - `config.vm.provision "file", source: "./provision.sh", destination: "$HOME/"`
        - copies a `file` from the source to the detination. `$HOME/` is the variable for the home directory
    - `config.vm.provision "shell", inline: "sudo chmod +x provision.sh && sudo ./provision.sh", run:"always"`
        - runs a shell inline and gives `provision.sh` the permission to execute and(&&) runs it as sudo

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
- line 17 to 27 on app shows in condtions
    - says connect to database if it exists
    - and show us on /posts page


## Questions
- is it better to run the script from local or copy it over and run
- in a vagrant file how to I got back to a machine already set up and run code after setting another up