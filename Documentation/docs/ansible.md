[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)  
[IaC local task](/Documentation/docs/IaC_local_task.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)  
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  

## Ansible
- Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. Ansible’s goals are foremost those of simplicity and maximum ease of use.

- benefits
    - Human readable automation (easy to use)
        - YAML
    - Powerful with a high level of configuration
    - Agentless
        - uses OpenSSH and WinRM
        - runs on your controller, no need to install elsewhere
    - cross-platform support

## Hostfile
This is your inventory of computers that ansible can connect to and interact with.

example:
```
[aws]
ec2-instance ansible_host=63.34.20.247 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem
```
if you're having interrupter problems you can add:
```
[local]
localhost ansible_python_interpreter=/usr/local/bin/python3
```
## Playbooks
An Ansible® Playbook is a blueprint of automation tasks—which are complex IT actions executed with limited or no human involvement. Ansible Playbooks are executed on a set, group, or classification of hosts, which together make up an Ansible inventory.
playbooks are written in yaml, also used by:
- docker
- compose
- kubernetes
- cloud formation
- store them in /etc/ansible

## Ansble ad-hoc command
Ansible ad-hoc commands are a way to interact with the hosts without making a playbook.
`ansible all -m ping`
[adhoc cheat sheet](/Documentation/resources/IaC/Ansible-Cheat_Sheet_Edureka.pdf)

## Security with aws
You can set up three layers of security

### Ansible vault
- Secure storage for aws keys
- it used the vi editor
- make /etc/ansible/group_vars/all
- sudo ansible-vault create pass.yml
    - i to go to insert mode
```
aws_access_key: <ACCESS KEY>
aws_secret_key: <SECRET KEY>
```
- esc, :wq!
- sudo cat pass.yml
- sudo chmod 666 pass.yml


### pem key
- cd ~/.ssh
- sudo nano eng114.pem
- paste eng114.pem key content from localhost
    - in automation you'll need to copy this over 
- sudo chmod 400 eng114.pem

### ssh key
- ssh-keygen -t ed25519 -C "dav.par.code@gmail.com"
- eng114
- enter
- enter

### using the key
`sudo ansible-playbook create_ec2.yml --ask-vault-pass --tags create_ex2`
- runs playbook (make playbook)
- asks for password to vault
password

## how to install
```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get update
sudo apt-get install ansible -y
```