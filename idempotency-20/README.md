# Идемпотетность и коммутативность API в HTTP и очередях 

📚 Домашнее задание/проектная работа разработано(-на) для курса "[Microservice Architecture](https://otus.ru/lessons/microservice-architecture/)"

## Описание
При создание заказа проверяется ключ идемпотентности. 

Тесты:
1. Регистрация пользователя
1. Логин пользователя
1. Создание заказа: ошибка нехватки денег
1. Пополнение счета
1. Создание заказа: Успешно
1. Создание заказа: ошибка request-id должен быть уникален

## Запуск

```
minikube start
minikube addons enable ingress

# namespace: default
kubectl apply -f manifest
```

## Проверка
```
newman run otus.postman_collection.json
```


