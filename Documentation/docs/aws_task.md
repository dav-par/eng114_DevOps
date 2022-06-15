
## Setting up a EC2 on AWS
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


## to script a file text change
- sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mongod.conf
    - `-i` rewrites the file
    - replaces 127.0.0.1 with 0.0.0.0 in the mongodb config file
- https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux




# accessing s3 via awscli
- `aws s3 ls`
    - shows all the buckers we can access
- `aws configure`
    - the core command to configure where you can add your keys and region
- then use `aws s3` followed by the code

- common aws s3 commands
- `aws s3 mb s3://eng114-david-bucket`
    - make a bucket
    - naming convention is `-`
- `aws s3 cp test.txt`
    - copy file to bucket
- `aws s3 cp s3://eng114-david-bucket/test.txt my_copied_file.ext`
    - copies a file from the bucket to the machine you ran the command from
- `aws s3 sync s3:/eng114-david-bucket .`
    - syncs the full bucket to the machine you ran the command from 
- `aws s3 rm s3:eng114-david-bucket/test.text`
    - removes the file from the bucket
- `aws s3 rb s3://eng113-david`
    - removes the bucket

- s3 api
s3 has an api which I havn't used

- accessing sc3 via python scripts using awscli
I found the easyiest way to do is to work on localhost then scp the scripts over
`scp -i "eng114.pem" -r /c/git_projects/eng114_DevOps/Python/boto3/  ubuntu@ec2-18-203-110-71.eu-west-1.compute.amazonaws.com:`
- link to scripts


## Setting up a topic
- 

## Setting up an EC2 to use AWS
- click the instance in the EC2 menu
- Actions
- Monitor and troubleshoot
- Manage cloudwatch alarms
- Create an alarm
- name alarm
- choose your notificaion method (topic)
- Alarm actions - optional
- Alarm threshold
    - maximum (single data point over value)
    - cpu utilisation
    - alarm when >= 30
    - 1 period for 1miniute
    - name 

## setting up launch template
- 

## Setting up autoscalling and load balancing
- Create an Auto Scalling Group
- Choose template
- Choose subnets in VPC (1a, 1b, 1c)
- Attach to a new load balancer (eng114-david-asg-app2-2)
    - internet facing
    - listening on port 80
    - grace period 300
    - enable group metrics
    - create a target group
configure group size
    - 2,2,3
Scaling policy
    - target tracking policy
    - average cpu utilizaton
    - target value 30
    - instant needs 300
notifications
    - david cpu
tag
    - eng114-david-automade




[google sre book](https://sre.google/sre-book/monitoring-distributed-systems/#:~:text=The%20four%20golden%20signals%20of,system%2C%20focus%20on%20these%20four)


## notes
- aws will issue a new ip to an instance if it's off for more than an 30mins
- the curl 6.0 script installed nodejs 8.x and not 6.x
- the curl script doesn't install npm and needs to be done manually  
![node and npm version screenshot](/Documentation/resources/app_node_version.png)
- #TODO -expand on notes


