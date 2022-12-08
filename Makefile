build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose restart

run: down build up

db-shell:
	docker-compose exec db psql -U postgres
