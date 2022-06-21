[link to index](/readme.md)  
# cicd task using jenkins
![jenkins pipeline](/Documentation/resources/cicd/jenkins_diagram.png)

## Documentation
- [click here](/Documentation/docs/cicd.md)  

## Prerequisite
- app folder in a separate repo - [mine](https://github.com/dav-par/eng114_app)  
- office 365 connector
- github plugin
- github publisher

## SSH to github
- [git hub instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- `git remote set-url origin <SSH url>`
    - can be used to change the way you you push to an already cloned repo
    - good for keeping your `.gitignore` etc


## Build jenkins job for app
- new item
    - name
    - freestyle project
    - add
- configure
    - General  
        - discard old builds
            - 3 max build
        - github project
            - https link 
                - `https://github.com/dav-par/eng114_app.git`
    - Office 365 Connector
        - restrict where project can be run
            - `sparta-ubuntu-node`
    - source code management
        - see below for ssh
        - choose branch to build
    - build environment
        - node and npm
            - installation: Sparta-Node-JS
            - npmrc file - system default
            - cach location - Default (~/.npm or %APP DATA% pm-cache)
    - build
        ```
        cd app
        npm install
        npm test
        ```

## SSH from github to jenkins
- make an ssh key on your local host
    - `ssh-keygen -t ed25519 -C "email@host.com"`
- go to the github repo you want to automate and add the public key
    - settings
    - deploy keys
    - add public key
- go to the config of the jenkins file and add the private key to job
    - source code management
    - git
    - repo url `SSH code link to github repo`
    - Credentials
        - add key
        - jenkins
        - kind - ssh
        - username - group-name
        - private key - enter directly
        - add

## github webhooks
- config file of the jenkins job
    - build triggers
        - github hook trigger for gitscm polling
- github repo settings
    - webhooks
        - payload url
            - jenkins-server/github-webhook
            - `http://0.0.0.1:8080/github-webhook/`
        - content type
            - json
        - triggers
            - select individual events
                - pushes
                - pull requests

## Job to push dev to main once successfully tested
- create dev branch on local host and push to github
    - `git branch dev`
    - `git checkout dev`
    - `git push --set-upstream origin dev`
- create new job `name-merge-dev-to-main`
    - set up as above
    - source code management git
        - ssh to repo as before
        - build main branch
        - additional behaviours
            - merge before build
                - name of repo `origin`
                - branch to merge to `dev`
                - merge strategy `default`
                - fast-forward mode `-ff`
- create a job that builds dev branch
- post-build actions
    - git publisher
        - push only if build succeeds
        - merge results
        - branch to push `main`
        - target remote name `origin`


## Job to push working build to EC2

- prerequisites
    - repo with:
        - app
        - default file for nginx
        - jenkins app provisioning script - [link](https://github.com/dav-par/eng114_app/blob/main/jenkins_provision.sh)
- set up and ec2
    - own vpc
    - public subnet
    - security groups
        - ssh from local (22)
        - http from all (80)
        - app from all (3000)
        - ssh from jenkins (port 22, jenkins ip server/32)
- set up jenkins job
    - description
    - discard old build
        - max 3 builds
    - github project
        - https link to app repo
    - source code manangment
        - Git
            - ssh git with repo key
            - main branch
    - build triggers
        - Build after other projects are build
            - your merge job
        - SSH agent
            - aws pem key
    - build
        - execute shell
            ```
            #!/bin/bash
            ls
            rsync -avz -e "ssh -o StrictHostKeyChecking=no" . ubuntu@34.244.68.124:
            ssh -A -o "StrictHostKeyChecking=no" ubuntu@34.244.68.124 << EOF
            chmod +x jenkins_provision.sh
            sudo ./jenkins_provision.sh
            ```