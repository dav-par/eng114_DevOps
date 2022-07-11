# Ansible
holding file for ansible content

## Hostfile
- this is your inventory of computers that ansible can connect too
- layout
```
[aws]
ec2-instance ansible_host=63.34.20.247 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/eng114.pem
```
- if you're having interrupter problems you can add:
```
[local]
localhost ansible_python_interpreter=/usr/local/bin/python3
```



- ## Security with aws
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
<asks for password to vault>
password