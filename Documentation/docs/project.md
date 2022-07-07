# project
We want to automate launching the app using:
- Jenkins as a controller
- Docker to run containers across EC2s
- DockerHub to host our images of:
    - app
    - db

![First attempt at architecture](/Documentation/resources/project/first_draft.png)


## Step one
- set up a jenkins server
- I followed the steps in my jenkins set up [here](/Documentation/docs/jenkins_task.md)
- I installed the following plugins:
    - terraform
        - configure in global plugins
    - ansible
    - docker

## Step two - use terraform to set up two ec2s
- install terraform plugin
- install terraform via the global plugin
- install terraform via ssh on jenkins server

