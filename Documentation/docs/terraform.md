[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)  
[IaC Terraform task](/Documentation/docs/terraform_task.md)  
 
# Terraform
- HashiCorp Terraform is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share.
- You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. Terraform can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features.
- benefits
    - open source
    - simple syntax
    - modularity
    - multi-cloud
    - immutable and version control built in
- installing
    - put the exe somewhere easy to find and run it
    - update the path to include the folder the exe is in

## Common commands
- `terraform init`
- `terraform plan`
- `terraform apply`
- `terraform destroy`

# extra commands
- `terraform apply -auto-approve`
- `terraform destroy -target aws_instance.app_instance -target aws_instance.db_instance`

## how to install
