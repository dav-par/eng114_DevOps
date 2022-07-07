[link to index](/readme.md)  
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)  
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  
[IaC Terraform task](/Documentation/docs/terraform.md)    
# IaC task
- set up 3 machines using vagrant
    - [vagrant file](/IaC_ansible/original_vagrantfile)
    - ssh in to each and update and upgrade
    - `sudo apt update -y && sudo apt upgrade -y`
    - install ansible on the controller
```
sudo apt-get update -y
	
sudo apt-get install software-properties-common
	
sudo apt-add-repository ppa:ansible/ansible -y
	
sudo apt-get update
	
sudo apt-get install ansible -y
```
- ssh in to both machines manually from the controller to add the public keys
- in the controller still
- `ssh vagrant@192.168.33.10`
- `yes`
    - add key
- `vagrant`
    - password
- same for db
- configure them using ansible
    - add web and db machine to the host file
    - `sudo nano /etc/ansible/hosts`
    - add to the bottom
```
[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
```

- `ansible all -m ping`
    - to test connection
    - should get green pong response
- `cd /etc/ansible/`
    - navigate to ansible folder
- `sudo git clone -b vagrant https://github.com/dav-par/working_ansible.git` to get the scripts
-  `sudo mv ansible/* ansible/.* .` - moves scripts down a level
- run these scripts on the controller
    - nginx, proxy, node, config 
- they will set up the webserver
- ` ansible-playbook nginx.yml` etc
- ssh to web machine and run
    - cd app/app/
    - sudo npm install
    - npm start

## questions
- why are we in the ansible folder
- can we automate adding the ssh keys
- can we update/upgrade in the vagrant file
- can we automate gitclone and script running


## Updated task
- fully automated from `vagrant up` 
- use this [vagrant file](/IaC_ansible/Vagrantfile) in a folder with this [provisioning script](/IaC_ansible/local_controller_pro.sh)
    - launches all three machines
    - updates && upgrades the web and db machine
    - installs ansible on the controller
    - copies over the provisioning script to the controller and runs it there
- the script
    - updates && upgrades
    - installs ansible and dependencies
    - clones a github repo with
        - the app folder
        - default file to set up a reverse proxy
        - config file for mongodb to allow it to accept all connections
        - 6 ansible playbooks
    - runs the playbooks which set up the db and web machine
    - launches the app on the web machine
- go to http://192.168.33.10/posts on your web browser to see if it worked in full