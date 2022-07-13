[index](/readme.md)  
[IaC](/Documentation/docs/IaC.md)    
[IaC hybrid task](/Documentation/docs/IaC_hybrid_task.md)  
[IaC cloud task](/Documentation/docs/IaC_cloud_task.md)  

# IaC local task
Set up the app and db on two local virtual machines using a third virtual machine as an ansible controller.


## Set up three machines
- Use this [vagrant file](/IaC_ansible/original_vagrantfile) and name it Vagrantfile
- ssh in to each and update and upgrade
- `sudo apt update -y && sudo apt upgrade -y`
- ssh into the controller
    - install ansible on the controller
    - ssh into both machines manually from the controller to add them to your known hosts
    - `ssh vagrant@192.168.33.10` (ip of app machine)
    - `yes`
        - adds the key to the known hosts
    - `vagrant`
        - password
    - same for db
- add the two machines to your host file
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

## Configure the app and db using ansible playbooks
- `cd /etc/ansible/`
    - navigate to ansible folder
- `sudo git clone -b vagrant https://github.com/dav-par/working_ansible.git` to get the scripts
-  `sudo mv ansible/* ansible/.* .`
    - moves scripts down a level
- run these scripts on the controller
    - ` ansible-playbook nginx.yml` etc
    - nginx, proxy, node, config 
- they will set up the webserver

## check it works
- ssh to web machine and run
    - cd app/app/
    - sudo npm install
    - npm start
- go to http://192.168.33.10/posts on your web browser to see if it worked in full

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