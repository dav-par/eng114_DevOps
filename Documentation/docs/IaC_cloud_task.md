[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)

# IaC cloud task
set up the controller in the cloud which can create both the app and db instances on separate EC2s set

## set up the controller on ec2
- log in to aws and set up a controller EC2 instance
    - with ubuntu 18.04
    - that you can ssh into
    - with this [user data](https://github.com/dav-par/eng114_DevOps/blob/main/IaC_ansible/cloud_task/controller_pro.sh)
        - update && upgrade
        - installs ansible
        - installs python, pip and boto3
        - git clones scripts, host file and config files - [here](https://github.com/dav-par/working_ansible)
        - makes group_vars/all
- scp the key you'll be using from a terminal in your local host .ssh folder
    - `scp -i "david_eng114.pem" -r david_eng114.pem ubuntu@ec2-52-208-3-247.eu-west-1.compute.amazonaws.com:~/.ssh`

## set up ansible vault and AWS access
- ssh into the controller
- `cd /etc/ansible/group_vars/all`
- `sudo ansible-vault create pass.yml`
    - creates a protected file that you edit with vim
    - press i
        - vim insert command
    - copy the code below and add your keys
```
aws_access_key: <ACCESS KEY>
aws_secret_key: <SECRET KEY>
```
-    
    - press esc
    - type `:wq!` and press enter
        - exits the vim editor and saves (writes)
    - `sudo cat pass.yml`
        - should post random chars if working
    - `sudo chmod 666 pass.yml`
        - means that all users can read and write but cannot execute the file/folder
    - `cd ~/.ssh`
    - `sudo chmod 400 david_eng114.pem`
    - ssh-keygen -t rsa
    - eng114
    - enter
    - enter

## prepare the playbooks
- edit the app playbooks to include:
    - correct key name
    - unique id
    - public subnet
    - security group for app on public subnet
    - refer to aws_access_key
    - correct pem key in ec2 provisioning 
- same for db
    - use a pre loaded db ami as it won't have internet access
    - private subnet and db security group
- make sure the groups are named app and db in the hostfile

## run creation playbooks
- `sudo ansible-playbook 7_create_app_ec2.sh --ask-vault-pass --tags create_ec2`
    - creates the ec2 for the app
    - vault password
- `sudo ansible-playbook 8_create_db_ec2.sh --ask-vault-pass --tags create_ec2`
    - creates the ec2 for the db
    - vault password

## add the EC2s to the host file
- add the ip
- add the ssh key
```
[app]
app-ec2 ansible_host=54.194.156.130 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem

[db]
db-ec2 ansible_host=172.31.26.178 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem`
```

## run playbooks
run playbooks in order 1 to 6

## check it works
go to the public ip of the app machine/posts to check

## errors
- fatal: [localhost]: FAILED! => {"changed": false, "msg": "Instances with id(s) ['i-0c2154f122e72388c'] were created previously but have since been terminated - use a (possibly different) 'instanceid' parameter"}
    - you need to change the instant name