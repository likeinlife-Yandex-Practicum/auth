# Запуск 
up:
	docker compose up -d --build

env:
	cp sample.env .env

# Остановка
downv:
	docker compose down -v

down:
	docker compose down

# Тестирование
test:
	docker compose -f tests/docker-compose.yaml up --build --abort-on-container-exit --exit-code-from tests --attach tests

down-test:
	docker compose -f tests/docker-compose.yaml down

# Миграции 
makerevision:
	docker compose exec api alembic -c /opt/app/alembic.ini revision --autogenerate -m $(NAME)

migrate:
	docker compose exec api alembic -c /opt/app/alembic.ini upgrade head

# CLI
create-admin:
	docker compose exec api python -m cli admin create $(email) $(password)

