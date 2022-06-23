# IaC task
- set up 3 machines using vagrant
    - [vagrant file](/IaC_ansible/Vagrant/Vagrantfile)
    - ssh in to each and update and upgrade
`sudo apt update -y && sudo apt upgrade -y`
    - install ansible on the controller
```
sudo apt-get update -y
	
sudo apt-get install software-properties-common
	
sudo apt-add-repository ppa:ansible/ansible -y
	
sudo apt-get update
	
sudo apt-get install ansible -y

- ssh in to both machines mannaully from controller to add public key

```

- configure them using ansible
    - add web and db machine to the host file
`sudo nano /etc/ansible/hosts`
    - add to the bottom
```
[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
```

- run `ansible all -m ping` to test connection
- nav to /etc/ansible/
- `sudo git clone https://github.com/dav-par/ansible` to get the scripts
-  `sudo mv ansible/* ansible/.* .` - moves scripts down a level
- run these scripts on the controller
    - nginx, proxy, node, 
- they will set up the webserver
- ` ansible-playbook nginx.yml` etc
- ssh to web machine and run
    - sudo npm install
    - npm start