[link to index](/readme.md)  
[link to K8 task](/Documentation/docs/kubernetes_task.md)  
# Kubernetes (K8)
K8 is an open source orchestration tool.

## K8 Components
A Kubernetes cluster consists of the components that represent the control plane and a set of machines called nodes.

## objects
Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Specifically, they can describe.

## services
An abstract way to expose an application running on a set of Pods as a network service.
With k8 you don't need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

## cluster
A Kubernetes cluster is a set of node machines for running containerized applications. If you’re running Kubernetes, you’re running a cluster.

## etcd
The consistent and highly-available key-value store used as Kubernetes' backing store for all cluster data.

## installing
There are many ways to do so, the quickest is to use docker desktop with the k8 extension activated which does all the heavy lifting
[![Docker desktop and k8](/Documentation/resources/k8/docker_desktop_k8.png)](https://www.docker.com/blog/how-kubernetes-works-under-the-hood-with-docker-desktop/)



## architecture 
![components](/Documentation/resources/k8/components-of-kubernetes.svg)  
![etcd](/Documentation/resources/k8/stacked-etcd.svg)  

