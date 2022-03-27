saga:
	cd saga && make -f ../Makefile run

store:
	cd store && make -f ../Makefile run

finder:
	cd finder && make -f ../Makefile run

finder_consumer:
	cd finder && python manage.py consumer

transaction:
	cd transaction && make -f ../Makefile run

delivery:
	cd delivery && make -f ../Makefile run

notifications:
	cd notifications && make -f ../Makefile run

notifications_consumer:
	cd notifications && python manage.py consumer

wait_db:
	bash /app/wait-for $(DATABASE_HOST):$(DATABASE_PORT) -- echo db connect

create_db:
	echo "SELECT 'CREATE DATABASE $(DATABASE_NAME)' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$(DATABASE_NAME)')\gexec" | PGPASSWORD=$(DATABASE_PASSWORD) psql -h $(DATABASE_HOST) -U $(DATABASE_USER)

run: wait_db create_db
	python manage.py migrate && python manage.py runserver 0:8000

makemigrations:
	cd saga && python manage.py makemigrations
	cd transaction && DATABASE_NAME=transaction python manage.py makemigrations
	cd notifications && DATABASE_NAME=notifications python manage.py makemigrations

migrate:
	cd saga && python manage.py migrate
	cd transaction && DATABASE_NAME=transaction python manage.py migrate
	cd notifications && DATABASE_NAME=notifications python manage.py migrate

.PHONY: saga store transaction delivery finder finder_consumer notifications notifications_consumer
.PHONY: create_db run makemigrations
