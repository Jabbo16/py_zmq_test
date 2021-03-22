# py_zmq_test
This is a simple test on how to implement zmq in Kubernetes clusters.
We use kind for running local Kubernetes clusters using Docker containers.

How to use this repo:

1. create kind clusters

```
kind create cluster --config config.yaml
```

2. create pods

```
kubectl apply -f zmq_deployment.yaml
```

3. set up Metallb (we use LoadBalancer as the service type)

Create the metallb namespace 

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/namespace.yaml
```

4. use service to expose the application
```
kubectl apply -f zmq_service.yaml
```
