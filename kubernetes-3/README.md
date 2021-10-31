# Основы работы с Kubernetes (часть 3)

📚 Домашнее задание/проектная работа разработано(-на) для курса "[Microservice Architecture](https://otus.ru/lessons/microservice-architecture/)"

## Запуск
```
minikube start
minikube addons enable ingress
kubectl create namespace myapp
kubectl config set-context --current --namespace=myapp
kubectl apply -f manifest
```

## Проверка
```
newman run user.postman_collection.json
```