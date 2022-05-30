## Vagrantup
-https://www.vagrantup.com/intro

Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.

### Common commands
- `vagrant init` intialise first install of a box
- `vagrant reload` = reloads the config file whilst keeping the system up

### Setting up vagrant with a config file
- `vagrant up` - load file
- `vagrant ssh` - ssh in 
- `sudo apt-get update` update system
- `sudo apt-get upgrade` upgrade system
- `sudo apt-get install nginx -y` - install nginx
- open `192.168.10.100` in browser to test it