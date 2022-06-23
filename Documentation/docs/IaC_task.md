# IaC task
- set up 3 machines using vagrant
    - [vagrant file](/IaC_ansible/Vagrant/Vagrantfile)
    - ssh in to each and update and upgrade
`sudo apt update -y && sudo apt upgrade -y`
- configure them using ansible
    - add web and db machine to the host file
`sudo nano /etc/ansible/hosts`
    - add to the bottom
`[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant

[db]
192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant`
    - run `ansible all -m ping` to test connection
    - [ansible repo](https://github.com/dav-par/ansible)
    - run these scripts on the controller
    - they will set up the webserver