Prometheus. Grafana 

📚 Домашнее задание/проектная работа разработано(-на) для курса "[Microservice Architecture](https://otus.ru/lessons/microservice-architecture/)"

## Запуск
```
minikube start
minikube addons enable ingress
kubectl create namespace myapp
kubectl config set-context --current --namespace=myapp

kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install -n monitoring prom prometheus-community/kube-prometheus-stack -f prometheus.yaml --atomic
kubectl apply -f manifest
```

## Команды
**Grafana**, user:password - admin:prom-operator
```
minikube service -n monitoring prometheus-grafana-nodeport
```
**Prometheus**
```
minikube service -n monitoring prom-prometheus-nodeport
```

## Dashboard
Manigest [grafana.yaml](manifest/grafana.yaml).
![](grafana.PNG)


