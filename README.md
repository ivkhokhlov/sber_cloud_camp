# QASberCloud - test
## Введение

Тестовое задание для QACloudCamp
https://github.com/QACloudCamp/test-assignment

## Зависимости
Для запуска этого проекта необходимо иметь установленные:
	- Python 3.11 (не тестировалось на других версиях)
	- Poetry - инструмент для управления зависимостями Python

## Установка и настройка
### Установка Poetry
Если у вас ещё нет установленного Poetry, вы можете установить его, используя следующую команду:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### Клонирование репозитория
Клонируйте репозиторий с помощью git:
```bash
git clone https://github.com/ivkhokhlov/sber_cloud_camp.git
cd sber_cloud_camp
```
### Установка зависимостей проекта
Используйте следующую команду для установки зависимостей проекта:
```bash
poetry install
```
### Установка локального json-server
Для простоты можно использовать готовый докер-образ:
```bash
docker run --rm -p 3000:3000 svenwal/jsonplaceholder
```
### Запуск тестов
По умолчанию тесты запускаются для локально развернутого `json-server`, т.к. для публичной версии https://jsonplaceholder.typicode.com имеются ограничения CRUD операций и часть тестов будут падать.
Для запуска с локально запущенным сервером:
```bash
poetry run -m pytest
```
или
```bash
poetry run -m pytest --host http://localhost:3000
```
Для запуска с публичным общедоступным сервером
```bash
poetry run -m pytest --host https://jsonplaceholder.typicode.com
```
## Использование с Docker
### Сборка образа
Перейти в директорию с проектом и собрать образ
```bash
cd /path/to/prjct
docker build -t pytest_cloud .
```
### Запуск тестов
для локального сервера
 ```bash
docker run --rm pytest_cloud
```
для запуска с произвольным адресом сервера использовать `--host`
```bash
docker run --rm pytest_cloud --host https://jsonplaceholder.typicode.com
```
