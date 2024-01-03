# Запуск 
up:
	docker compose -f docker-compose-dev.yaml up -d --build

# Остановка
downv:
	docker compose -f docker-compose-dev.yaml down -v

down:
	docker compose -f docker-compose-dev.yaml down

# Тестирование
test:
	docker compose -f tests/docker-compose.yaml up --build --abort-on-container-exit --exit-code-from tests --attach tests

down-test:
	docker compose -f tests/docker-compose.yaml down

# Миграции 
makerevision:
	docker compose -f docker-compose-dev.yaml exec auth-service alembic -c /opt/app/alembic.ini revision --autogenerate -m $(NAME)

migrate:
	docker compose -f docker-compose-dev.yaml exec auth-service alembic -c /opt/app/alembic.ini upgrade head

# CLI
create-admin:
	docker compose -f docker-compose-dev.yaml exec auth-service python -m cli admin create $(email) $(password)

