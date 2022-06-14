#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.7 -y
sudo apt install python3-pip -y
sudo pip3 install awscli
python3.7 -m pip install boto3 #not tested, may need alias python=python3.7 first
#Type the below commands manually as they requre alias which can't be scripted
#alias python=python3.7
#aws configure
#access key
#secret key
#eu-west-1
#json
