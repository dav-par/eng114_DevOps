[index](/readme.md)  
[K8 doc](/Documentation/docs/kubernetes.md)  
## run a K8 cluster on AWS
- create an ec2 instance
- ubuntu 18.04
- t2.medium
- public subnet
 -public ip
- 10gig
- pem key
- below commands
    - some of these will need approval but can probably be automated in a script
```
sudo apt update -y && sudo apt upgrade -y
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce -y

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube


sudo usermod -aG docker $USER && newgrp docker

minikube config set driver docker #didn't work

minikube start --driver=docker

minikube kubectl -- get po -A

alias k="minikube kubectl --"
```



first try:
```
sudo apt update -y
sudo apt upgrade -y
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
sudo apt update -y
sudo apt upgrade -y
sudo apt-get install -y docker.io
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
&& chmod +x minikube \
&& sudo mv minikube /usr/local/bin/
git clone https://github.com/dav-par/k8_cloud.git
```
alias k=kubectl
k create -f all.yml
sudo minikube start --driver=docker --force

https://phoenixnap.com/kb/install-kubernetes-on-ubuntu


sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```