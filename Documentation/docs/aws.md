[link to index](/readme.md)  
# AWS
- AWS is the cloud computing offer from amazon
- It has regions all over the world
    - a region is typically a geographic area or city such as London
- Each region has availability zones (AZs)
    - These are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones.
    - This reduces the chance of failure by not having a single point.
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


## Amazon Simple Storage Service (S3)
S3 is a global object storage solution provided by amazon.
- global
- s3 file permissions (r,w,rw,x,public,owner,readonly)
- uses aws keys, secure them
    - awscli
    - terraform vault
- benefits
    - can store anything
    - no data limit
    - global service
        - highly available
        - highly scalable
    - Good for disaster recovery
- storage classes
    - standard (high cost)
        - can access data 24/7 (actively available)
    - glacier (less cost)
        - available on request with notice
        - usually 24 hours
- S3 uses cases
    - disaster recovery plan
        - github is a cloud and can go down
        - s3 is a good backup
    - social media
        - can host anything
        - is economical
- was on aws certification 3/5 questions

## Amazon Web Service Command Line Interface
AWS CLI is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts. It works with python3 and pip3.

- Set up
    - update
    - upgrade
    - sudo apt-get install python-pip -y
    - sudo apt install python3-pip
    - alias python=python3
    - sudo pip3 install awscli
    - aws configure #This encrypts the keys
        - access key
        - secret key
        - region
            - eu-west-1
        - output
            - json
    - Now use the keys to access s3


## amazon machine images AMIs
- these are images of a machine in a certain state
- you can save your machine, terminate it and bring it back from an image
- you may need to start some services up depending on how the image was saved

## Security groups
- these are saved firewall states you can apply to an AWS instance
- they control what ports can access what on the machine

## editing permissions
- can be on the control panel
- can be on awscli
- can be in python

## monitoring 
- We will need to make a system to monitor our aws instances when it's running
- aw has sns cloud watch (simple notification system)
- we can check if the status code isn't 200 and then use a load balancer to keep the app running
- if the app goes down and the users notice we will lose business
- the role of DevOps is to build the infrastructure that doesn't have a single point of failure 
- make your emergency plan part of sdlc
- devops is monitoring  and fixing automatically

## Four golden rules
The four golden signals of monitoring are latency, traffic, errors, and saturation. If you can only measure four metrics of your user-facing system, focus on these four. The time it takes to service a request. It's important to distinguish between the latency of successful requests and the latency of failed requests.  

- latency
    - the time it takes for a service request
- traffic
    - how much demand for your service
- errors
    - the rate of requests that fail etc
- saturation
    - how 'full' your service is

## services
- CLOUDWATCH
- SNS simple notification service
- SQS simple queue service

## Autoscaling
AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. 

## Load balancer
- Directs the traffic to different instances of the same thing
- Application load balancer
    - good for network-facing app
- Elastic load balancer
- Network load balancer   

## Autoscaler
![autoscaler](/Documentation/resources/aws/auto_scaler.jpeg)


## General notes
- aws will issue a new ip to an instance if it's off for more than 30mins
- the curl 6.0 script installed nodejs 8.x and not 6.x
- the curl script doesn't install npm and needs to be done manually  
![node and npm version screenshot](/Documentation/resources/app_node_version.png)
- #TODO -expand on notes


