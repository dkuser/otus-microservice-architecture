# Распределенные транзакции

📚 Домашнее задание/проектная работа разработано(-на) для курса "[Microservice Architecture](https://otus.ru/lessons/microservice-architecture/)"

## Цель проекта
Разработка интернет-магазина, включая:
- Разработка независимых сервисов заказа, билинга, доставки, поиска и нотификаций с отдельными базами данных
- Использование патерна Saga для формирование заказа
- Синхронизация данных между сервисами через Kafka


Что получилось:
1. Регистрация/логин пользователя (OrderService)
1. Управление товарами (StoreService)
1. Пополнение счета (TransactionService)
1. Управление доставкой (DeliveryService)
1. Поиск товара (FinderService)
1. Создание/отмена заказа (OrderService)
1. Просмотр логов (NotificationService)
1. Мониторинг (Grafana)


## Запуск

```
minikube start
minikube addons enable ingress
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install kafka bitnami/kafka
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prom prometheus-community/kube-prometheus-stack -f prometheus.yaml --atomic

# namespace: default
kubectl apply -f manifest

# saga: http://arch.homework/
# kafka-ui: http://arch.homework/kafkaui/
# pg: kubectl port-forward service/postgres 5433:5432
```

## Команды
**Grafana**, user:password - admin:prom-operator
```
minikube service prometheus-grafana-nodeport
```
**Prometheus**
```
minikube service prom-prometheus-nodeport
```

## Проверка
```
newman run project.postman_collection.json
```