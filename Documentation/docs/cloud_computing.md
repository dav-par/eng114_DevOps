# Cloud Computing/
Cloud computing is the practice of using a network of remote servers hosted on the internet to store, manage, and process data, rather than a local server or a personal computer.

## Benefits
- Shared responsbility
- Security
- High scalability
- High availability 
- Low capital expendeture
- Low operational expenditure

## Why you should use it
- You only pay for what you need
- If you're planning to have lots of users

## When you shouldn't use it
- you have the faclities to host it
- it's not a critical system
- it's for a small user base

[Inside a google data center youtube video](https://www.youtube.com/watch?v=XZmGGAbHqa0)


## AWS
- AWS is the cloud computing offer from amazon
- It has regions all over the world
    - a region is typically a geographic area or city such as London
- Each region has avliablity zones (AZs)
    - These are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones.
    - This reduce the chance failure by not having a single point.
- Considerations when choosing a region
    - who is the end user? client? clients customers?
    - where is the end user
    - how often are they going to use it
    - server latency
    - local data laws (gdpr etc)
- cloud servers from amazon we use:
    - london for ci/cd pipeline
    - irland for devops
    - frankfurt for data training
- Our naming convention:
    - eng114_name_app
    - eng114_name_db
    - eng114_name_bastion
    - etc
