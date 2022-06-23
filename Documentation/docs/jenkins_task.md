# Hosting and updating an app with jenkins and aws
This is a step by step on how to set up a jenkins server that can automate the ci/cd process of installing and updating an app. In this iteration we will set up the ec2 manually.


Prerequisites
- vpc with a public subnet

## setting up  a jenkins server
- https://www.jenkins.io/doc/book/installing/linux/
- setting up the machine
    - log in to the aws panel and navigate to the ec2 page for your region
    - launch an instance with:
        - Ubuntu Server 18.04 LTS (HVM)
        - t2.micro
    - configure instance details
        - vpc network
        - public subnet
        - public ip
    - 10 gig storage
    - tagged so you can find it
    - security groups
        - port 80 for all
        - port 8080 for all
        - port 22 for your ip
- configuring jenkins via ssh
    - ssh in and run the these commands
    - `sudo apt update -y && sudo apt upgrade -y`
        - updates and upgrades the machine
    - `sudo apt install openjdk-11-jre -y`
        - install java
    - `sudo nano set_up.sh`
        - copy the below code in to the set_up.sh script
        -  this installs the latest stable version of jenkins
```
#!/bin/bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```
- `sudo chmod +x set_up.sh`
    - this lets the file run as an executable
- `sudo ./set_up.sh`
    - this runs the file
- `sudo systemctl enable jenkins`
    - this sets jenkins to run on boot
- `sudo systemctl start jenkins`
    - this starts jenkins

## configuring the server
- got to the ip of your server on port 8080
- `sudo cat /var/lib/jenkins/secrets/initialAdminPassword`
    - via ssh to get the password
- install suggested plugins
- make an admin account
- leave the address alone

- manage jenkins
- manage plugins
- click available
- search for and install
    - ssh agent
    - nodejs
- restart
- log in
- manage jenkins
- Global tool configuration
    - add nodejs
    - name nodejs
    - version 13.3.0


## full userdata to install jenkins on a blank ec2
```
#!/bin/bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install openjdk-11-jre -y
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```