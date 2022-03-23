saga:
	cd saga && python manage.py runserver 0:8000

store:
	cd store && python manage.py runserver 0:8000

finder:
	cd finder && python manage.py runserver 0:8000

finder_consumer:
	cd finder && python manage.py consumer

transaction:
	cd transaction && python manage.py runserver 0:8000

delivery:
	cd delivery && python manage.py runserver 0:8000

notifications:
	cd notifications && python manage.py runserver 0:8000

notifications_consumer:
	cd notifications && python manage.py consumer

.PHONY: saga store transaction delivery finder finder_consumer notifications notifications_consumer
