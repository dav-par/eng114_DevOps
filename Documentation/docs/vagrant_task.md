[link to index](/readme.md)  
# Set up vagrant multibox
#TODO info on task

## provision file for test app
- Firstline
    - `#!/bin/bash`
        - tells the os it's a script and to use bash to run it
- #update and upgrade
    - `sudo apt-get update -y`
        - updates the package list with the latest available versions
    - `sudo apt-get upgrade -y`
        - upgrade command actually upgrades and installs the latest versions of packages that are already installed.
- #install nginx
    - `sudo apt-get install nginx -y`
        - installs the webserver nginx and skips the yes/no prompt
- #start nginx and make sure it runs from boot
    - `sudo systemctl start nginx`
        - starts the webserver
    - `sudo systemctl enable nginx`
        - tells the webserve to stay on
- #Install Node.js 6.x repository
    - `curl -sL https://deb.nodesource.com/setup_6.x | bash -`
        - curl gets data from a server via url
        - `-s` to do it silently, `-L` makes it follow any links
        - `|` pipes the data from the url in to bash
        - `bash` runs the script file
        - `-` #TODO
- #Install Node.js and npm 
    - `apt-get install -y nodejs`
        - uses the apt-get package manager to install `nodejs` which was grabbed by curl, which includes `npm` the worlds largest software registry
        - `-y` skips the yes/no prompt
    - `npm install pm2 -g`
        - uses `npm` to install `pm2` a nodejs process manager
        - `-g` installs it globally
- #navigate to app folder and use npm to install the app
    - `cd app/app`
        - navigates to the folder with the app
    - `npm install`
        - tells npm to install it
    - `npm start -d`
        - tells npm to start the app
        - `-d` sets up in detached mode so you can run other commands in the background


## Set up the machine
- set up your vagrant file
- set your provisions file
- run vagrant up/

## How to set up a reverse proxy for the app
we want to use reverse proxy to forward port 3000 to port 80 for easy of use for our users so they don't have to type :3000 after the ip

- `sudo nano /etc/nginx/sites-available/default`
    - this access the default file for the webserver
- In the file change the location block and follow the indentation:
```
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
- `nginx -t`
    - to check the config
- `sudo systemctl restart nginx`
    - to restart the webserver with the new config/
- this needs to be automated in the provisioning file

## Connecting to the database
- line 17 to 27 of the app.js shows an if statement:
    - if DB_HOST is present then render the /posts page
- so we need to build the DB_HOST machine and then set the envriomental variable on the app machine
- we will use mongodb as our database
- the app runs on port 3000, mongodb runs on port 27017
- after updating the config we will need to `restart` and `enable` mongodb
-

## Setting up the mongodb
- we will use ubuntu 16.04, the same as our app machine
- configure the machine:
    - allow app ip to connect to db machine
    - install correct version of mongodb
    - the default config file only lets 127.0.0.1 connect, we will change this to the app machine ip or 0.0.0.0 (this will allow any connection)
    - `mongo --eval 'db.runCommand({ connectionStatus: 1 })'` will check if mongod is running

## mongodb provision file here
#TODO

## changing the mongodb config file
- navigate to etc folder
- `sudo nano mongod.conf`
- change ip to 0.0.0.0

## restart the mongodb
- `sudo systemctl restart mongod`
- `sudo systemctl enable mongod`


## finish setting up the app
- once we have the ip (192.168.10.15) of the db machine we can save an enviroment variable in the .bashrc file
- `sudo echo "export DB_HOST=mongodb://192.168.10.150:27017/posts" >> ~/.bashrc`
- `source ~/.bashrc`
- this is because the app refers to DB_HOST
- we can test it with `printenv DB_HOST`
- #TODO how to edit, how to script
- we can now run the app with `nohup node app.js > /dev/null 2>&1 &` #TODO explain