[link to index](/readme.md)  
# cicd task using jenkins
![jenkins pipeline](/Documentation/resources/jenkins_diagram.png)  

## Documentation
- [click here](/Documentation/docs/cicd.md)  

## SSH to github
- [git hub instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- `git remote set-url origin <SSH url>`
    - can be used to change the way you you push to an already cloned repo
    - good for keeping your `.gitignore` etc

## make second key
public key to github  
private key to jenkins  
ssh-keygen -t ed25519 -C "email@host.com"  

## github webhooks
-

## jenkins jobs
- jobs are the name of any task you set in jenkins
- you can make a job to do anything you would do locally such as run scrips
- you can make one job trigger another
- making a job
    - new item
    - create job
    - fill in task

## Multistage Build with Jenkins
- 
