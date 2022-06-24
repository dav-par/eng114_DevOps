# IaC hybrid task
controller local
nodes online

keys
chmod
folder structure


- Set up the controller
    - run the vagrant file and provisioning script
        - [here](/IaC_ansible/)
        - updates && upgrades
        - installs ansible
        - installs python, pip and boto3
        - clones my playbook folder
        - makes group_vars/all
    - `cd /etc/ansible/group_vars/all`
    - `sudo ansible-vault create pass.yml`
        - set vault password
        - press i
            - vim insert commmand
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
    - `nano eng114.pem`
        - replace `eng114` with your aws pem key name
    - paste eng114.pem key content from localhost
        - in automation you'll need to copy this over 
    - `sudo chmod 400 eng114.pem`
    - ssh-keygen -t rsa
    - eng114
    - enter
    - enter

## run playbooks
- `cd /etc/ansible/`
- `sudo mv playbook.yml group_vars/`
- `cd group_vars`
- `sudo ansible-playbook playbook.yml --ask-vault-pass --tags create_ec2`
    - runs the ec2 creation playbook
- vault password

## errors
- fatal: [localhost]: FAILED! => {"changed": false, "msg": "Instances with id(s) ['i-0c2154f122e72388c'] were created previously but have since been terminated - use a (possibly different) 'instanceid' parameter"}
    - you need to change the instant name
