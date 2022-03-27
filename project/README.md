# Распределенные транзакции

📚 Домашнее задание/проектная работа разработано(-на) для курса "[Microservice Architecture](https://otus.ru/lessons/microservice-architecture/)"

## Описание
Паттерн «Сага» на примере интернет магазина. 

Тесты:
1. Создание товара в сервисе Склад
2. Установка баланса в сервисе Платеж
3. Создание заказа -> Ошибка в сервисе Склад
4. Создание заказа -> Ошибка в сервисе Платеж
5. Проверка в сервисе Склад -> Остатки уменьшились
6. Отмена заказа
7. Проверка в сервисе Склад -> Остатки восстановились
8. Создание заказа -> Ошибка в сервисе Доставка
9. Проверка в сервисе Платеж -> Баланс уменьшился
10. Отмена заказа
11. Проверка в сервисе Платеж -> Баланс восстановился
12. Создание свободного курьера
13. Создание заказа -> Заказ успешно создан

## Запуск

```
minikube start --cpus=4 --memory=4g
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
newman run Saga.postman_collection.json
```