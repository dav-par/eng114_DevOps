[index](/readme.md)  
[K8 doc](/Documentation/docs/kubernetes.md)  
# run app and db with K8
- Set up the app and db using K8
- [here](/docker/k8/) in one block
- run all the code in one block
- see below


## set up
- `swtich on k8 in docker desktop`
- `kubectl get service - kubectl get ssvc`
- `kubectl get deployment - kubectl get deploy`
- `kubectl get pods`
- `kubectl cluster-info`


## Task
- `kubectl create -f all.yml`
  - once set up run the below code in a yaml file

# code block
```
apiVersion: apps/v1
kind: Deployment # pod, service, replicateset # ASG

metadata:
  name: db
spec:
#lables and selectors are communicaiton channels between microservices
  selector:
    matchLabels:
      app: db
  replicas: 1
  template:
    metadata:
      labels:
        app: db
    spec: 
      containers:
        - name: db
          image: mongo
          resources:
            limits:
              memory: 512Mi
              cpu: "1"
          ports:
            - containerPort: 27017
          imagePullPolicy: Always

---
apiVersion: v1
kind: Service
metadata:
  name: db
  namespace: default
spec:
  ports:
    -  port: 27017
       protocol: TCP
       targetPort: 27017
  selector:
    app: db

---
apiVersion: apps/v1
kind: Deployment # pod, service, replicateset # ASG

metadata:
  name: node
spec:
#lables and selectors are communicaiton channels between microservices
  selector:
    matchLabels:
      app: node
  replicas: 3
  template:
    metadata:
      labels:
        app: node
    spec:
      containers:
        - name: node
          image: davparcode/eng114_app:v3
          env:
          - name: DB_HOST
            value: mongodb://db/posts
          resources:
            limits:
              memory: 512Mi
              cpu: "1"
          ports:
            - containerPort: 3000
          imagePullPolicy: Always

---
apiVersion: v1
kind: Service
metadata:
  name: node
  namespace: default
spec:
  ports:
  - nodePort: 30400 # 30000 - 302222
    port: 3000
    protocol: TCP
    targetPort: 3000
  selector:
    app: node
  type: NodePort # cluster - LoadBalancer
  ```