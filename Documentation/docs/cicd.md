[link to index](/readme.md)  
# cicd
CICD is considered the backbone of DevOps practices and automation, It plays vital, challenging and exciting role in DevOps culture, and growing numbers of companies releasing software in minutes with the adoption of CICD practices.

![cicd workflow](/Documentation/resources/cicd/cicd_workflow.png)  

## What is a CICD Pipeline
The CI/CD pipeline is all about automation: Initiating code builds, automated testing, and automated deploying to the staging or production environments. It’s complex and exciting at the same time, but incredibly fast, if the output of any stage fails, the next stage will also fail.

## Benefits of CICD pipeline
- Reduce risk
- Deliver faster
- Expend less manual effort
- Generate extensive logs
- Make easier rollbacks

## Continuous Integration (CI)
Developers merge/commit code to the master branch multiple times a day, fully automated build and test process which gives feedback within a few minutes, by doing so, you avoid the integration h#ell that usually happens when people wait for release day to merge their changes into the release branch.

## Continuous Delivery (CD)
Continuous Delivery is an extension of continuous integration to make sure that you can release new changes to your customers quickly in a sustainable way. This means that on top of having automated your testing, you also have automated your release process and you can deploy your application at any point of time by clicking on a button. In continuous delivery, the deployment is completed manually.

## Continuous Deployment (CDE)
Continuous Deployment goes one step further than continuous delivery, with this practice, every change that passes all stages of your production pipeline is released to your customers, there is no human intervention, and only a failed test will prevent a new change to be deployed to production.

## key difference
- in CD the deployment is done manually, in CDE the deployment is also automated
- CD is good when the business has controlled releases or wants to wait for a time with less user load e.g. bank phone app
- CD is best if the risk is so high that deployment going wrong is greater than the risk of "slow-release"
- CDE is good for things which need to be updated quickly e.g. security update
- CDE is good for services that need 100% uptime or they will lose business e.g. netflix, amazon, ebay

## what is jenkins
The leading open-source automation server, Jenkins provides hundreds of plugins to support building, deploying and automating any project.

![jenkins pipeline](/Documentation/resources/cicd/jenkins.png)  

## jenkins jobs
- jobs are the name of any task you set in jenkins
- you can make a job to do anything you would do locally such as run scrips
- you can make one job trigger another
- making a job
    - new item
    - create job
    - fill in task

## tools for CICD pipeline
![cicd tools](/Documentation/resources/cicd/cicd_tools.png)  


## Why Jenkins
Multi-Billion Dollar companies like Facebook, Netflix and Ebay have adopted Jenkins because of it’s amazing advantages, Jenkins is an open-source automation server in which the central build and CI process take place, It is a Java-based program with packages for Windows, macOS, & Linux.

- tech
    - open source
    - great plugins
    - can be integrated with most cloud platforms
    - good for working out cicd requirements
- business
    - faster processes means your product gets to market quicker
    - cheap to use (opensource)

## when not to use cicd
- if it will cost too much
- if you've not planned
- for non-repetitive or rarely repeated tasks 
