# py_zmq_test
This is a simple test on how to implement zmq in Kubernetes clusters.
We use [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) for running local Kubernetes clusters using Docker containers.

How to use this repo:

1. create kind clusters

```
kind create cluster --config config.yaml
```

2. create pods

```
kubectl apply -f zmq_deployment.yaml
```

3. set up Metallb (we use LoadBalancer as the service type), ref: https://kind.sigs.k8s.io/docs/user/loadbalancer/.

Create the metallb namespace 

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/namespace.yaml
```

Create the memberlist secrets 

```
kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)" 
```

Apply metallb manifest

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/metallb.yaml
```

Check address pool used by loadbalancers
```
docker network inspect -f '{{.IPAM.Config}}' kind
```

4. use service to expose the application
```
kubectl apply -f zmq_service.yaml
```

5. Now the pods and service should be running. We can interact with pods using ```kubectl exec -ti pod-name /bin/bash```. Python code containing zmq pub/sub applications can be found via ```cd /home```.
