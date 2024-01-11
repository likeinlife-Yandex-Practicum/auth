# Описание

Auth service сделан для авторизации и работы с ролями пользователей

# Авторы
* [@likeinlife](https://github.com/likeinlife)
* [@maxim-zaitsev](https://github.com/maxim-zaitsev)

## Вклад @likeinlife

- OAuth: Google, Yandex
- CRUD, API: User, UserRole
- JWT
- Tests
- Migrate to SQLModel
- CLI

В последующем спринте понадобился этот сервис, в этот момент также изменил логику обработки ошибок.
Было: try/except в каждой ручке
Стало: все ошибки приложение наследуются от базового класса, на который повешен обработчик fastapi exception

# Вклад @maxim-zaitsev

- Nginx
- Models
- CRUD, API: Role, AccountHistory

# Установка

- Скопировать файл `./docker-composes/.env.example` в файл `./docker-composes/.env`
- через Makefile выполнить команды:
  - `make env` - подготовит .env
  - `make up`
  - `make migrate`
  - `make create-admin email=<email> password=<password>`

# Запуск/остановка

- `make up` - запуск
- `make down` - удалить созданные контейнеры
- `make downv` - удалить созданные контейнеры, включая volumes

# Тестирование

- `make test`
- `make down-test`

# URLs

- auth: http://localhost/auth/api/openapi
- jaeger: http://localhost:16686/
