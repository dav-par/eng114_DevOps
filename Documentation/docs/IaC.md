[link to index](/readme.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)  
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  
[IaC Terraform task](/Documentation/docs/terraform_task.md)  
[Terraform](/Documentation/docs/terraform.md)  
[Ansible](/Documentation/docs/ansible.md)  

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
