#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.7 -y
sudo apt install python3-pip -y
sudo pip3 install awscli
alias python=python3.7
python -m pip install boto3
#aws configure
#access key
#secret key
#eu-west-1
#json