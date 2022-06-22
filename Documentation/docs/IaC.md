# Infrastructure as Code (IaC)
IaC is the process of using code to provision computers, usually hosted at a data center. The machine-readable code will tell the hardware exactly what environment it needs. In best practice, the code is version controlled so you can call on the exact version you need

- benefits
    - cost
        - having the code saved means once you've got a working environment you don't need to go through the process of finding all the parts again
        - code requires fewer people and effort to maintain which saves cost
    - speed
        - automating machines is quicker than doing it manually
    - risk mitigation
        - as it is automated it removes the risk for human error
        - version control means it is less likely you'll provide the wrong machine or forget what was needed in the past


## tools available
![IaC tools](/Documentation/resources/IaC/tools.png)  
![IaC tool stages](/Documentation/resources/IaC/tools2.png)  
![IaC tool comparison](/Documentation/resources/IaC/tools3.png)  

## Configuration management and orchestration under IaC

- Configuration management (e.g. Ansible)
    - configuring a server using a tool like chef, puppet or ansible
    - happens repeatedly, unlike provisioning which is usually a one-off
    - it brings consistency to the infrastructure
 
- orchestration (e.g. Terraform)
    - arranging or coordinating multiple systems
    - running the same task on lots of servers at once but not necessarily all of them

- comparison
    - Configuration orchestration tools, which include Terraform and AWS CloudFormation, are designed to automate the deployment of servers and other infrastructure.
    - Configuration management tools like Chef, Puppet, and the others on this list help configure the software and systems on this infrastructure that has already been provisioned.

## Ansible
- Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. Ansible’s goals are foremost those of simplicity and maximum ease of use.

- benefits
    - Human readable automation (easy to use)
    - Powerful with a high level of configuration
    - Agentless
        - uses OpenSSH and WinRM
        - no agent to exploit or update

## Terraform
- With Terraform, we describe our complete infrastructure as code, even as it spans multiple service providers. Our servers may come from AWS, our DNS may come from CloudFlare, and our database may come from Heroku. Terraform will build all these resources across all these providers in parallel.


## Ansible and Terraform in DevOps
- this is a form of provisioning plus Configuration Management
- Terraform will deploy the underlying infrastructure including:
    - network topology
    - data stores
    - load balancers
    - servers
- Ansible then deploys the app to that hardware 

- benefits
    - a fully automated process using robust tools

