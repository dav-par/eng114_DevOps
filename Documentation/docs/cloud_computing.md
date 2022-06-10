# Cloud Computing
Cloud computing is the practice of using a network of remote servers hosted at a remote site to store, manage, and process data, rather than a local server or a personal computer.

## Benefits
- Shared responsbility
- Security
- High scalability
- High availability 
- Low capital expendeture
- Low operational expenditure

## Why you should use it
- You only pay for what you need
- If you're planning to have lots of users

## When you shouldn't use it
- you have the faclities to host it
- it's not a critical system
- it's for a small user base

[Inside a google data center youtube video](https://www.youtube.com/watch?v=XZmGGAbHqa0)


## AWS
- AWS is the cloud computing offer from amazon
- It has regions all over the world
    - a region is typically a geographic area or city such as London
- Each region has avliablity zones (AZs)
    - These are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones.
    - This reduce the chance failure by not having a single point.
- Considerations when choosing a region
    - who is the end user? client? clients customers?
    - where is the end user
    - how often are they going to use it
    - server latency
    - local data laws (gdpr etc)
- cloud servers from amazon we use:
    - london for ci/cd pipeline
    - irland for devops
    - frankfurt for data training
- Our naming convention:
    - eng114_name_app
    - eng114_name_db
    - eng114_name_bastion
    - etc

## mointering 
- We will need to make a system to monitor our aws instances when it's running
- aw has sns cloud watch (simple notification system)
- we can check if the status code isn't 200 and then use a load balancer to keep the app running
- if the app goes down and the users notice we will lose business
- the role of DevOps is to build the infrastructure that doesn't have a single point of failure 

## Setting up a AWS
- rent an ec2 server
- we need to know
    - family
        - t2 micro
    - hard drive
    - security
        - allow port 22 for ssh from localhost
        - allow port 80 so anyone can see the webserver
        - port 3000 for the app
    - migrating the app and db
        - use scp to secure copy `scp -i "eng114.pem" ~/db_provision.sh ubuntu@ec2-54-229-164-96.eu-west-1.compute.amazonaws.com:` (we could use rsync)
    - create a secure ssh key


## Setting up app instance
- click ec2
- launch instance
- Ubuntu Server 18.04 LTS (HVM), SSD Volume Type (note the upgrade from 16 on vm)
- t2 micro
- configure
    - default 1a subnet #TODO-why
    - enable public ip
    - 8 gig
- tag
    - key: Name
    - value: eng114_name_app
- security groups
    - 22 for ssh from localhost ip
    - 80 from anywhere to host the app
    - 3000 for the app
- ssh in to machine from .ssh folder with the downloaded private key
    - key downloaded
    - ip found in aws pannel
    -`ssh -i "eng114.pem" ubuntu@ec2-54-220-95-85.eu-west-1.compute.amazonaws.com`
- from localhost copy over app and provision script
    - `scp -i "eng114.pem" ~/app_provision.sh ubuntu@ec2-54-229-164-96.eu-west-1.compute.amazonaws.com:`
    - check script and run
        - #TODO link to script
    

![two tier app set up](/Documentation/resources/two_tier_aws_app.png)


## set up ssh and app machine
- set up machine as above
- copy your ssh key to the `.ssh` folder
- `chmod 400 my-key-pair.pem`
    - set the key to read only (amazon requirment)
- `ssh -i "~/.ssh/david_ssh.pem" ubuntu@ec2-13-40-135-50.eu-west-2.compute.amazonaws.com`
    - ssh to app machine to see if it works
- open new terminal (localhost_terminal)
- `scp -i "~/.ssh/david_ssh.pem" -r ~/aws_setup/app_setup ubuntu@ec2-13-40-135-50.eu-west-2.compute.amazonaws.com:`
    - Copy app and provision script over securly using ssh
- `cd /app_setup`
    - navigate to app setup folder
- `sudo ./app_provision.sh`
    - run the provisioning script
- open new terminal and set up db

## setting up the db
- set up machine:
    - allow app to connect
    - allow localhost to shh in (port 22)
    - allow default port access for mongodb 27017
    - db must not have public access
- `ssh -i "~/.ssh/david_ssh.pem" ubuntu@ec2-18-169-191-57.eu-west-2.compute.amazonaws.com`
    - ssh to db machine to see if it works
- in your localhost terminal
- `scp -i "~/.ssh/david_ssh.pem" -r ~/aws_setup/db_setup ubuntu@ec2-18-169-191-57.eu-west-2.compute.amazonaws.com:`
    - Copy monogodb config and provision script over securly using ssh
- `cd /db_setup`
    - navigate to app setup folder
- `sudo ./db_provision.sh`
    - run the provisioning script #TODO - link script and explain
- Note: currently the db is open to all ips 0.0.0.0
    - this is bad practice

## Finish setting up app
- `export DB_HOST=mongodb://34.245.119.223:27017/posts`
    - sets the enviroment variable DB_HOST
    - use the public ip of the db machine
    - should be added ~/.bashrc
- `node seeds/seed.js`
    - seeds the db
- `cd ~/app/app`
    - navigate to app folder 
- `nohup node app.js > /dev/null 2>&1 &`
    - runs the app in the background
-  `source ~/.bashrc`
        - refreshs the file

## amazon machine images AMIs
- these are images of a machine in a certain state
- you can save your machine, teminate it and bring it back from an image
- you may need to start some services up depending on how the image was saved
    - `sudo nano ~/.bashrc`
        - open `.bashrc` for the user in nano 
    - update the line `export DB_HOST=mongodb://52.212.95.36/posts` with the latest ip
    - `source ~/.bashrc`
        - refreshs the file
        - `printenv DB_HOST` to check it worked
        - note: make sure to edit the user `.bashrc` as this is checked first before `bash.bashrc` in the `/etc` folder
- nohup node app.js > /dev/null 2>&1 &

## What are security groups
- these are saved firewall states you can apply to an AWS instance
- they control what ports can access what on the machine

## notes
- aws will issue a new ip to an instance if it's off for more than an 30mins
- the curl 6.0 script installed nodejs 8.x and not 6.x
- the curl script doesn't install npm and needs to be done manually 
![node and npm version screenshot](/Documentation/resources/app_node_version.png)
- #TODO -expand on notes