[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)

# IaC cloud task
set up an ansible controller which can automatically launch the app and db with a click 

## set up the controller on ec2
- [run the provisioning script](https://github.com/dav-par/eng114_DevOps/blob/main/IaC_ansible/controller_pro.sh)
    - update && upgrade
    - installs ansible
    - installs python, pip and boto3
    - git clones scripts and host file
    - makes group_vars/all
- `scp -i "david_eng114.pem" -r david_eng114.pem ubuntu@ec2-52-208-3-247.eu-west-1.compute.amazonaws.com:~/.ssh`
    - run this on localhost from .ssh folder to copy your key to the ec2 instance
- ssh into the controller
- `cd /etc/ansible/group_vars/all`
- `sudo ansible-vault create pass.yml`
    - set vault password
    - press i
        - vim insert command
    - copy the code below and add your keys
```
aws_access_key: <ACCESS KEY>
aws_secret_key: <SECRET KEY>
```
-    
    - press esc
    - type `:wq!`
    - `sudo cat pass.yml`
    - `sudo chmod 666 pass.yml`
    - `cd ~/.ssh`
    - `sudo chmod 400 david_eng114.pem`
    - ssh-keygen -t rsa
    - eng114
    - enter
    - enter
- `cd /etc/ansible/` #moving scripts to right place
- `sudo mv 7_create_app_ec2.sh group_vars/`
- `sudo mv 8_create_db_ec2.sh group_vars/`

## prepare the playbooks
- app playbook
    - unique id
    - public subnet
    - security group for app on public subnet
    - refer to aws_access_key
    - correct pem key in ec2 provisioning 
- same for db
    - private subnet and db security group

## run creation playbooks
- [here](https://github.com/dav-par/working_ansible)
- `cd /etc/ansible/group_vars`
- `sudo ansible-playbook 7_create_app_ec2.sh --ask-vault-pass --tags create_ec2`
    - creates the ec2 for the app
    - vault password
- `sudo ansible-playbook 8_create_db_ec2.sh --ask-vault-pass --tags create_ec2`
    - creates the ec2 for the db
    - vault password

## add to host file
- app group
    - `ec2-instance ansible_host=3.251.86.93 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/david_eng114.pem`
- db2 group
    - `ec2-instance2 ansible_host=3.251.86.93 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/david_eng114.pem`

## edit playbooks
- change web to app in app playbooks
- change db to db2 in db playbooks

## run playbooks
run playbooks in order 1 to 6

## errors
- fatal: [localhost]: FAILED! => {"changed": false, "msg": "Instances with id(s) ['i-0c2154f122e72388c'] were created previously but have since been terminated - use a (possibly different) 'instanceid' parameter"}
    - you need to change the instant name