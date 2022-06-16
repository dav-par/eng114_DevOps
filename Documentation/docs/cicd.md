# cicd
CICD is considered as the backbone of DevOps practices and automation, It plays vital, challenging and exciting role in DevOps culture, growing numbers of companies releasing software in minutes with the adoption of CICD practices.

![cicd workflow](/Documentation/resources/cicd_workflow.png)  

## What is a CI CD Pipeline
The CI/CD pipeline is all about automation: Initiating code builds, automated testing, and automated deploying to the staging or production environments. It’s complex and exciting at the same time, but incredibly fast, if the output of any stage fails, the next stage will also fail.

## Benifits of CICD pipeline
- Reduce risk
- Deliver faster
- Expend less manual effort
- Generate extensive logs
- Make eaiser rollbacks

## Continuous Integration (CI)
Developers merge/commit code to master branch multiple times a day, fully automated build and test process which gives feedback within few minutes, by doing so, you avoid the integration h#ell that usually happens when people wait for release day to merge their changes into the release branch.

## Continuous Delivery (CI)
Continuous Delivery is an extension of continuous integration to make sure that you can release new changes to your customers quickly in a sustainable way. This means that on top of having automated your testing, you also have automated your release process and you can deploy your application at any point of time by clicking on a button. In continuous Delivery the deployment is completed manually.

## Continuous Deployment
Continuous Deployment goes one step further than continuous delivery, with this practice, every change that passes all stages of your production pipeline is released to your customers, there is no human intervention, and only a failed test will prevent a new change to be deployed to production.

## key diffrence
- in CD the depoloyment is done manually, in CDE the deployment is also automated

## what is jenkins
The leading open source automation server, Jenkins provides hundreds of plugins to support building, deploying and automating any project.

![jenkins pipeline](/Documentation/resources/jenkins.png)  



## tools for CICD pipeline
![cicd tools](/Documentation/resources/cicd_tools.png)  


## Why Jenkins
Multi Billion Dollar companies like Facebook, Netflix and Ebay have adopted Jenkins because of it’s amazing advantages, Jenkins is an open-source automation server in which the central build and CI process take place, It is a Java-based program with packages for Windows, macOS, & Linux.

- tech
    - open source
    - great plugins
    - can be intergrated with most cloud platforms
    - good for working out cicd requirements
- business
    - faster proccess means your product gets to market quicker
    - cheap to use (opensource)

## when not to use cicd
- if it will cost too much
- if you've not planned
- for non repetitive or rarely repeated tasks 
