# Cloud Computing
Cloud computing is the practice of using a network of remote servers hosted on the internet to store, manage, and process data, rather than a local server or a personal computer.

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
        - use scp to secure copy ` scp -i "eng114.pem" ~/db_provision.sh ubuntu@ec2-54-229-164-96.eu-west-1.compute.amazonaws.com:` (we could use rsync)
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
- ssh in to machine from .ssh folder
    -`ssh -i "eng114.pem" ubuntu@ec2-54-220-95-85.eu-west-1.compute.amazonaws.com`


## notes
aws will issue a new ip to an instance if it's off for more than an 30mins
