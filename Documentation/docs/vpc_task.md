[link to index](/readme.md)  
# VPC Tasks

## Create VPC documentation
[click here](/Documentation/docs/vpc.md)

## Redploy two tier architecture on VPC
- Diagram first
- Create private subnet for monogodb
- Design the public subnet and app ec2 connecting to the private subnet and db ec2
- Rules
    - private ec2 and subnet must not have a public ip
- Notes
    - public subnet already made
    - private subnet and db ec2 should not have public IP
- Explain route table for private subnet
    - rules
    - do you need one
- Optional
    - create NACL for your subnets for an addtional layer

## Diagram
![first draft](/Documentation/resources/aws/vpc_first.png)  

## Prerequisites
To complete this task successfully you will need
- Fully scripted and seeded db ami - [my script to set up ami](/aws_setup/db_setup/aws_db_provision.sh)
- Full script to set up app on ec2 which starts the app automatically - [my script](/aws_setup/app_setup/aws_app_provision.sh)
- VPC set up with internet gateway. public subnet and route table
    - VPC (empty house)
        -Only use IP4
        - Use chosen CIDR block, in our case this is 10.0.0.4/16
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

## creating a private subnet for mongodb
- go to the vpc pannel on aws - [link for eu-west-1](https://eu-west-1.console.aws.amazon.com/vpc/home?region=eu-west-1#Home:)
    - check your region
- click subnets in the right pannel
- click create subnet
- choose your VPC
- name the subnet following naming convention
    - course-name-subnet-private
- No prefrence for Availability Zone
- Choose a valid IPc4 CIDR block
    - I used 10.0.16.0/24
    - if working with several people, agree on these in advance
- click create subnet

## Launching the mongoDB instance
- Go to the EC2 instances panel - [link](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#Home:)
- Launch instance
- Select your prepaired db AMI
- t2.micro
- Configure instance details
    - Choose your VPC
    - Choose your private subnet
    - make sure public IP is disabled
    - no userdata needed as the ami is ready
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
- change the acces ip to your app ip 10.0.5.251/32

## Route table
- private subnet
    - This isn't needed and ensures your db doesn't connect to the internet
- public subnet
    - click route tables in the VPC panel
    - create route
    - follow naming convention
    - select your vc
    - subnet associations
        - assoicate with your subnet
    - edit routes - attaching internet gateway, you may already have done this
    - first route
        destination 10.0.0.0/16
        target local
    - second route
        - destination 0.0.0.0/0
        - target is your internet gateway
 