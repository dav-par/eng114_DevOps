#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.7 -y
alias python=python3.7
sudo apt install python3-pip -y
sudo pip3 install awscli
python -m pip install boto3