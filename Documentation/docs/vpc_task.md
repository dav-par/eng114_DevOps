[link to index](/readme.md)  
# VPC Tasks

## Create VPC documentation
[click here](/Documentation/docs/vpc.md)

## Redeploy two-tier architecture on VPC
- Diagram first
- Create a private subnet for monogodb
- Design the public subnet and app ec2 connecting to the private subnet and db ec2
- Rules
    - private ec2 and subnet must not have a public ip
- Notes
    - public subnet already made
    - private subnet and db ec2 should not have public IP
- Explain route table for the private subnet
    - rules
    - do you need one
- Optional
    - create NACL for your subnets for an additional layer

## Diagram
![first draft](/Documentation/resources/aws/vpc_first.png)  

## Prerequisites
### To complete this task successfully you will need
- Fully scripted and seeded db ami - [my script to set up ami](/aws_setup/db_setup/aws_db_provision.sh)
- Full script to set up app on ec2 which starts the app automatically - [my script](/aws_setup/app_setup/aws_app_provision.sh)
- VPC set up with internet gateway. public subnet and route table
    - VPC (empty house)
        -Only use IP4
        - Use chosen CIDR block, in our case this is 10.0.0.0/16
    - IG
        - Create and attach to VPC
    - Subnet
        - Select VPC
        - add subnet ID
    - Route table
        - Select VPC
        - Create table
        - Attach VPC to IG
        - Associate with subnet
    - an agreed IPv4 CIDR block to create your private subnet on
    - More details instructions to follow

## creating a vpc (empty house)
- name using convention
- IPv4 CIDR manual input
    - use your chosen CIDR block
    - 10.0.0.4/16
- no IPv6
- tag using name

## Creating an internet gateway and attaching it to the vpc
- create internet gateway
- tag following convention
- attach to your vpc

## subnets
- Create two subnets
- both on your vpc
- public
    - name using convention and add public
    - no preference for AZs
    - IPv4 CIDR block
        - add a valid unused subnet
        - 10.0.74.0/24
    - tag using name
- private
    - name using convention and add private
    - IPv4 CIDR block
        - 10.0.75.0/24
    - tag using name

## Route table
- private subnet
    - This isn't needed and ensures your db doesn't connect to the internet
- public subnet
    - click route tables in the VPC panel
    - create route table
    - follow naming convention
    - select your vc
    - subnet associations
        - edit subnet associations
        - associate with your subnet
    - edit routes - attaching internet gateway
        - first route
            destination 10.0.0.0/16
            target local
        - second route
            - destination 0.0.0.0/0
            - target is your internet gateway
    

## creating a private subnet for mongodb
- go to the vpc panel on aws - [link for eu-west-1](https://eu-west-1.console.aws.amazon.com/vpc/home?region=eu-west-1#Home:)
    - check your region
- click subnets in the right panel
- click create subnet
- choose your VPC
- name the subnet following the naming convention
    - course-name-subnet-private
    - No preference for Availability Zone
- Choose a valid IPc4 CIDR block
    - I used 10.0.16.0/24
    - if working with several people, agree on these in advance
- click create subnet

## Launching the mongoDB instance
- Go to the EC2 instances panel - [link](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#Home:)
- Launch instance
- Select your prepared db AMI
- t2.micro
- Configure instance details
    - Choose your VPC
    - Choose your private subnet
    - make sure public IP is disabled
    - no userdata is needed as the ami is ready
- 8gig
- Tag following naming convention
    - course-name-db-private-subnet
- Security groups
    - ssh 22 on "my ip"
    - custom TCP rule 27016 for app CIDR /32 ##not sure this works but good to try
        - once the app is up change this to the app EC2 private ip
    - outbound rules all open
        - this is automatically set
- Review and launch with course ssh key
- Your mongodb database is now:
    - hosted on an EC2
    - in a private subnet
    - not connected to the internet
    - has limited port access via security tables
- record the private IP
    - you'll need it to set up the app

## App set up
- launch an ec2 instance:
    - ubuntu 18.04
    - t2.micro
    - your vpc
    - your public subnet
    - public ip
    - user data script with the db private ip as DB_HOST
    - 8gig
    - taged following naming convention
    - security group
        - port 80 for all
        - port 22 for "my ip"
        - port 3000 for all (for the app)

## Finishing db set up
- go to your db security groups
- change the access ip to your app ip 10.0.5.251/32
