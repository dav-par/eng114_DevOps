[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)   
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  

# IaC hybrid task
Set up a controller in a local vm that configures two EC2s on aws with the app and db


## Set up controller
- run this [vagrant file](/IaC_ansible/hybrid_task/Vagrantfile)
    - updates && upgrades
    - installs ansible
    - installs python, pip and boto3
    - clones my playbook folder
    - makes group_vars/all

## Set up ansible vault and AWS access
- ssh in to controller `vagrant ssh controller`
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
    - `nano eng114.pem`
        - replace `eng114` with your aws pem key name
    - paste eng114.pem key content from localhost
        - in automation you'll need to copy this over 
    - `sudo chmod 400 eng114.pem`
    - ssh-keygen -t rsa
    - eng114
    - enter
    - enter

## get playbooks
- ssh into controller
- git clone https://github.com/dav-par/working_ansible.git

## create the two EC2s
- ssh into controller
- `cd /etc/ansible/`
- `sudo mv playbook.yml group_vars/`
- `cd group_vars`
- `sudo ansible-playbook 7_create_app_ec2 --ask-vault-pass --tags create_ec2`
    - runs the [app ec2 making playbook](https://github.com/dav-par/working_ansible/blob/main/7_create_app_ec2.yml)
- `sudo ansible-playbook 8_create_db_ec2 --ask-vault-pass --tags create_ec2`
    - runs the [db ec2 making playbook](https://github.com/dav-par/working_ansible/blob/main/8_create_db_ec2.yml)

## add the EC2s to the host file
- add the ip
- add the ssh key
```
[app]
app-ec2 ansible_host=3.251.86.93 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem

[db]
db-ec2 ansible_host=3.242.26.93 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem`
```

## run the rest of the playbooks on the respective instances
- nginx etc
- test by going to the app ip in a browser

## errors
- fatal: [localhost]: FAILED! => {"changed": false, "msg": "Instances with id(s) ['i-0c2154f122e72388c'] were created previously but have since been terminated - use a (possibly different) 'instanceid' parameter"}
    - you need to change the instant name
