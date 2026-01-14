# Kubernetes
What is Kubernetes? It is a tool used for the orchestration of containers.
**Minikube:** tool for running Kubernetes locally. The cluster that minikube creates has only one node in it.
**kubectl:** Kubernetes client
## Basic overview
1. Create a cluster
2. Deploy an app
3. Explore the app
4. Expose the app publicly
5. Scale up the app
6. Update the app
## Setting up minikube
1. Download and install minikube
2. Run `minikube start`
Automatically comes with kubectl as a subcommand, but an alias should be created: `alias kubectl="minikube kubectl --"`
### Control plane and nodes
The **control plane** manages the cluster while **nodes** are VMs or physical machines that serve as worker machines for the cluster. Nodes each have a kubelet that some process responsible for communicating with the control plane.
## Deploy an app
1. Switch to Docker environment: `eval $(minikube docker-env)`
2. Build application: `docker build -t tag .` -> now it's in the Minikube Docker environment
3. Define a `deployment.yml` file. Here is an example:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rag-app-deployment # A name...
spec:
  replicas: 1
  selector: # How the ReplicaSet finds with Pods to manage
    matchLabels:
      app: rag-api
  template:
    metadata:
      labels: # Labels for selecting the pods
        app: rag-api
    spec:
      containers:
      - name: rag-api-container
        image: rag-app
        imagePullPolicy: Never # When to pull a new image
        ports:
        - containerPort: 8000
        env:
        - name: OLLAMA_HOST
          value: "host.docker.internal:11434"
```
4. Apply the deployment: `kubectl apply -f deployment.yaml` - creates or updates resources defined in deployment.yaml
### Deployment
Blueprint of how an app should run. The app should always match the blueprint, so if a single container goes down, Kubernetes spins up a new container from the same image. Kubernetes is able to run copies, handle updates with no downtime, restart containers when they crash, and scale the app up and down. Technically, Kubernetes creates a ReplicaSet which creates Pods (i.e. running containers) and restarts them if they crash.
## Start a service
Each pod can be connected to, but a service provides stable IP addresses, a DNS name, load balancing, and automatic routing to healthy pods.
Example service:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: rag-app-service
spec:
  selector:
    app: rag-api
  ports:
  - port: 8000
    targetPort: 8000
  type: NodePort # Makes service accessible from outside the cluster
```
Apply service with: `kubectl apply -f service.yaml`
Start service: `minikube service local-rag-service
## Misc Commands
- Logs!! `kubectl logs <deployment name>`
	- Use `--previous` flag after to get logs from the previous instance of the deployment
- Restart deployment: `kubectl rollout restart deployment/<deployment name>`
- Delete deployment: `kubectl delete deployment <deployment name>`
## Other tips
- Pods, nodes, deployments, services, etc?