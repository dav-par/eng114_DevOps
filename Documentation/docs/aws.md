# AWS
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
        - highly avliable (trello card)
        - highly scalable (trello card)
    - Good for disaster recovery
- storage classes
    - standard (high cost)
        - can access data 24/7 (actively available)
    - glacier (less cost)
        - available on request with notice
        - usually 24 hours
- S3 uses cases
    - distaster recovery plan
        - github is a cloud and can go down
        - s3 is a good back up
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
    - aws configure #This encripts the keys
        - access key
        - secret key
        - region
            - eu-west-1
        - output
            - json
    - Now use the keys to access s3


## amazon machine images AMIs
- these are images of a machine in a certain state
- you can save your machine, teminate it and bring it back from an image
- you may need to start some services up depending on how the image was saved

## Security groups
- these are saved firewall states you can apply to an AWS instance
- they control what ports can access what on the machine

## eding permisons
- can be on control pannel
- can be on aws cli
- can be in python

## monitoring 
- We will need to make a system to monitor our aws instances when it's running
- aw has sns cloud watch (simple notification system)
- we can check if the status code isn't 200 and then use a load balancer to keep the app running
- if the app goes down and the users notice we will lose business
- the role of DevOps is to build the infrastructure that doesn't have a single point of failure 
- make your emergency plan part of sdlc
- dev ops is monitoring  and fixing automatically

## Four golden rules
The four golden signals of monitoring are latency, traffic, errors, and saturation. If you can only measure four metrics of your user-facing system, focus on these four. The time it takes to service a request. It's important to distinguish between the latency of successful requests and the latency of failed requests.  

- latency
    - the time it takes for a service request
- traffic
    - how much demand is on your service
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
- Directs the traffic to diffrent instances of the same thing
- Application load balancer
    - good for network facing app
- Elastic load balancer
- Network load balancer   

![auto-scale](/Documentation/resources/auto_scale.png)   
![auto-scale2](/Documentation/resources/auto_scale2.jpeg)   
![auto-load](/Documentation/resources/auto_load.png)




## Virtual Private Cloud (VPC)
A virtual private cloud (VPC) is a secure, isolated private cloud hosted within a public cloud. VPC customers can run code, store data, host websites, and do anything else they could do in an ordinary private cloud, but the private cloud is hosted remotely by a public cloud provider. (Not all private clouds are hosted in this fashion.) VPCs combine the scalability and convenience of public cloud computing with the data isolation of private cloud computing.

- why should we use it
    - because it is more fleixable than a standard network or VPN
    - you pay for what you use
    - they are more secure than a a public cloud

&nbsp;

- benefits of vpc
    - Scalability
        - Because a VPC is hosted by a public cloud provider, customers can add more computing resources on demand.
    - Easy hybrid cloud deployment
        - It's relatively simple to connect a VPC to a public cloud or to on-premises infrastructure via the VPN. (Learn about hybrid clouds and their advantages.)
    - Better performance
        - Cloud-hosted websites and applications typically perform better than those hosted on local on-premises servers.
    - Better security
        - The public cloud providers that offer VPCs often have more resources for updating and maintaining the infrastructure, especially for small and mid-market businesses. For large enterprises or any companies that face extremely tight data security regulations, this is less of an advantage.

&nbsp;

## Internet gateway
- A computer that sits between different networks or applications. The gateway converts information, data or other communications from one protocol or format to another. A router may perform some of the functions of a gateway. An Internet gateway can transfer communications between an enterprise network and the Internet.

## Subnet
- A subnet is a range of IP addresses within a network that are reserved so that they're not available to everyone within the network, essentially dividing part of the network for private use. In a VPC these are private IP addresses that are not accessible via the public Internet, unlike typical IP addresses, which are publicly visible.

## Classless Inter-Domain Routing (CIDR) block
- Classless Inter-Domain Routing (CIDR /ˈsaɪdər, ˈsɪ-/) is a method for allocating IP addresses and for IP routing. The Internet Engineering Task Force introduced CIDR in 1993 to replace the previous classful network addressing architecture on the Internet. Its goal was to slow the growth of routing tables on routers across the Internet, and to help slow the rapid exhaustion of IPv4 addresses.[1][2]
- [How to create one](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html)


##  Network Access Control Lists (NACL)
An optional layer of security that acts as a firewall for controlling traffic in and out of a subnet. You can associate multiple subnets with a single network ACL, but a subnet can be associated with only one network ACL at a time.

Security groups are associated with an instance of a service. It can be associated with one or more security groups which has been created by the user. NACL can be understood as the firewall or protection for the subnet. Security group can be understood as a firewall to protect EC2 instances.

In AWS, a network ACL (or NACL) controls traffic to or from a subnet according to a set of inbound and outbound rules. This means it represents network level security. For example, an inbound rule might deny incoming traffic from a range of IP addresses, while an outbound rule might allow all traffic to leave the subnet.

Because NACLs function at the subnet level of a VPC, each NACL can be applied to one or more subnets, but each subnet is required to be associated with one—and only one—NACL.

When you create a VPC, AWS automatically creates a default NACL for it. You can add and remove rules from a default NACL, but you can't delete the NACL itself.


When traffic enters your network, it is filtered by NACLs before it is filtered by security groups.

This means that traffic allowed by a NACL can then be allowed or denied by a security group, and traffic stopped by a NACL never makes it any further.

Given this "order of operations" in processing incoming traffic, here are two examples of implementing NACLs and security groups in tandem:

- use case of nacl
     - Use fine-grained rules with NACLs and let security groups handle inter-VPC connectivity.
        - For example, if you configure NACLs with granular rules for controlling inbound and outbound traffic, the NACLs can take the brunt of the work for filtering traffic. You can configure a NACL to allow inbound HTTP and HTTPS traffic from any IP address, deny all other inbound traffic, and allow all outbound traffic. As another example, you can allow inbound SSH access (port 22) from one IP address—yours—and allow outbound access on any port to the same IP address.
        
        Meanwhile, you can configure a security group to allow inbound traffic from itself, enabling communication between resources. Or, you can configure the security group to allow traffic into and out of a different security group, which enables instances within different subnets to talk to each other.

    - Eliminate whole classes of traffic with NACLs and use fine-grained rules with security groups.
        - In this scenario, you can configure a NACL to deny all traffic from a wide range of IP addresses to a certain protocol and port and allow the rest to continue to the security group, which may be configured to evaluate incoming and outgoing traffic on a more granular level. The NACL takes a coarse-grained approach to controlling traffic, leaving the security group to filter the rest through a fine-toothed comb.



## Diagram





## notes
- aws will issue a new ip to an instance if it's off for more than an 30mins
- the curl 6.0 script installed nodejs 8.x and not 6.x
- the curl script doesn't install npm and needs to be done manually  
![node and npm version screenshot](/Documentation/resources/app_node_version.png)
- #TODO -expand on notes


