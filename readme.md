# Eng114_DevOps
I have completed an intensive full-time DevOps course with Sparta Global, we covered the below topics.

# Index
## Core
[Linux](/Documentation/docs/linux.md)  
[Terminal](/Documentation/docs/terminal.md)  
[Git](/Documentation/docs/git.md)  
[vim](/Documentation/docs/vim.md)  

## Architecture
[Architecture](/Documentation/docs/architecture.md)  
[Cloud Computing](/Documentation/docs/cloud_computing.md)  
[Amazon Web Services (AWS)](/Documentation/docs/aws.md) - [task](/Documentation/docs/aws_task.md)  
[Virtual Private Cloud (VPC)](/Documentation/docs/vpc.md) - [task](/Documentation/docs/vpc_task.md)  
[Vagrant](/Documentation/docs/vagrant.md) - [task](/Documentation/docs/vagrant_task.md)  

## Infrastructure as Code
[Infrastructure as Code](/Documentation/docs/IaC.md)   
[Terraform](/Documentation/docs/terraform.md)  
[Ansible](/Documentation/docs/ansible.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)  
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  
[IaC Terraform task](/Documentation/docs/IaC_terraform_task.md)   
[Kubernetes](/Documentation/docs/kubernetes.md)  - [K8 local task](/Documentation/docs/k8_local_task.md) - [K8 cloud task](/Documentation/docs/k8_cluster_task.md)   
[Docker](/Documentation/docs/docker.md) - [task](/Documentation/docs/docker_task.md)  


## Continuous Integration and Continuous Delivery (CI/CD)
[Continuous Integration and Continuous Delivery (cicd)](/Documentation/docs/cicd.md)  
[cicd task](/Documentation/docs/cicd_task.md)  
[Jenkins setup](/Documentation/docs/jenkins_task.md) 

## Programming
[Object oriented programming](/Documentation/docs/oop.md)  
[Python](/Documentation/docs/python.md) - [code snippets](/Python/)  

## Other
[Unit testing](/Documentation/docs/unit_testing.md)  
[Misc notes](/Documentation/docs/misc.md)  

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