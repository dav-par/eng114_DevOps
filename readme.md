# Eng114_DevOps
I have started an intensive full-time DevOps course with Sparta Global, we have covered the below topics with more to come.

# Index
[Profile tips](/Documentation/docs/profile_tips.md)  
[Terminal/Linux](/Documentation/docs/terminal.md)  
[Git](/Documentation/docs/git_readme.md)  
[Architecture](/Documentation/docs/Architecture.md)  
[Cloud Computing](/Documentation/docs/cloud_computing.md)  
[cicd](/Documentation/docs/cicd.md) - [task](/Documentation/docs/cicd_task.md) - [jenkins setup](/Documentation/docs/jenkins_task.md)  
[AWS](/Documentation/docs/aws.md) - [task](/Documentation/docs/aws_task.md)  
[VPC](/Documentation/docs/vpc.md) - [task](/Documentation/docs/vpc_task.md)  
[vagrant](/Documentation/docs/vagrant.md) - [task](/Documentation/docs/vagrant_task.md)  
[Object oriented programming](/Documentation/docs/oop.md)  
[Python](/Documentation/docs/python_readme.md) - [code snippets](/Python/)  
[Unit testing](/Documentation/docs/unit_testing.md)  
[Misc notes](/Documentation/docs/misc.md)  
#

## What is DevOps  
DevOps is about bridging the gap between the developers and operations, using communication and consultancy to remove the blame culture and shifting the philosophical approach to software development from a start-stop waterfall to an infinite loop of continuous improvement.

![DevOps loop](/Documentation/resources/devops/devops_loop.png)

## Why DevOps - Benefits
DevOps helps in so many ways, the cultural as above but also brings in hard technical skills. These combined optimise the whole software development life cycle allowing everyone to focus on delivering a quality product to market.

### Key benefits
- Easy of use
    - Removing manual repetition removes human error
    - once set up you can launch your system with a few clicks
- Flexibility
    - once set up you can adapt to changes and update your environments as needed
- Robustness
    - There isn't a single point of failure
    - high availability
        - Your product is in the cloud with full backups ready to roll out if there's a problem at a data centre
    - high scalability
        - you can launch servers as needed to match user needs
- Cost
    - You only pay for what you need
    - Maintenance costs go down as so much is automated

[John Fahl has a great quote](https://medium.com/@jvftuo/my-journey-to-devops-eb655684a814)
>Then I watched the magic happen. He pushed a button on a Jenkins job, code for the automation was checkout of git, an AWS EC2 Instance was launched and test-kitchen ran through RSpec and Serverspec. Now, for those who aren’t tracking what all this means, I watched a vanilla server launched in the cloud, dozens of tests were run to validate the automation code, then acceptance tests were executed to actually configure the box and validate that it was, in fact, configured correctly. It didn’t stop there, the Chef cookbook launched an Elastic Load Balancer, created a certificate and attached it, and placed the server behind the load balancer. The cookbook did everything.

That is DevOps

## further benefits
- Speed, new requirements can be responded to quickly
- consistent environments
- Renews focuses on the customers
- Simplifies development focus
- Introduces automation to the development process
- Supports end-to-end responsibilityHappier teams leading to faster product shipments

## Role of DevOps
DevOps engineers build, test and maintain the infrastructure and tools to allow for the speedy development and release of the software. DevOps practices aim to simplify the development process of software.

## What is a development environment
A development environment is a controlled computer used to develop and test software, often in the form of a virtual machine with infrastructure as code.

- ## Why is it needed
    - To provide a consistent environment so the software can be accurately tested
    - Cheaper than running lots of real hardware

.