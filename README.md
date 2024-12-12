# Animal genetic

## API сервиса поиска работы Альфа

> RESTful API, ĸоторое позволяет сохранять данные генетичесĸих тестов животных,
> а таĸже выполнять подсчет агрегированной статистиĸи.

## Установка и запуск

Необходимые библиотеки:

- [Docker Compose](https://docs.docker.com/compose/)
- [GNU Make](https://www.gnu.org/software/make/)

Выполните следующие действия по порядку:

- Склонируйте репозиторий и перейдите в директорию проекта

```shell
git clone https://github.com/mign0n/animal_genetic.git && cd animal_genetic
```

- Создайте файл `.env`, при необходимости, отредактируйте его

```shell
cp .env.example .env
```

- Запустите контейнеры приложения (понадобятся root-права)

```shell
make run
```

- API будет доступен по адресу [http://0.0.0.0:9000](http://0.0.0.0:9000)

## API

API имеет две конечные точки:

1. POST /tests - для добавления данных

   ```shell
    curl --header "content-type:application/json" \
        --data '{
            "animal_name": "Дереза",
            "species": "коза",
            "test_date": "2024-07-18",
            "milk_yield": 3.2,
            "health_status": "good"
            }' \
        --request POST http://0.0.0.0:9000/tests/
   ```

   ```text
    {
       "id":6,"animal_name":"Дереза",
       "species":"коза",
       "test_date":"2024-07-18",
       "milk_yield":3.2,
       "health_status":"good"
    }
   ```

   GET /tests - для получения всех записей

   ```shell
   curl --header "content-type:application/json" \
       --request GET http://0.0.0.0:9000/tests/
   ```

   ```json
   [
     {
       "id": 1,
       "animal_name": "Буренка",
       "species": "корова",
       "test_date": "2024-12-09",
       "milk_yield": 28.5,
       "health_status": "good"
     },
     {
       "id": 2,
       "animal_name": "Зорька",
       "species": "овца",
       "test_date": "2024-12-09",
       "milk_yield": 0.0,
       "health_status": "good"
     },
     {
       "id": 3,
       "animal_name": "Гаврюша",
       "species": "теленок",
       "test_date": "2024-12-10",
       "milk_yield": 0.0,
       "health_status": "poor"
     },
     {
       "id": 4,
       "animal_name": "Мурашка",
       "species": "корова",
       "test_date": "2024-12-11",
       "milk_yield": 32.0,
       "health_status": "good"
     },
     {
       "id": 5,
       "animal_name": "Марфа",
       "species": "теленок",
       "test_date": "2024-12-11",
       "milk_yield": 0.0,
       "health_status": "good"
     },
     {
       "id": 6,
       "animal_name": "Дереза",
       "species": "коза",
       "test_date": "2024-07-18",
       "milk_yield": 3.2,
       "health_status": "good"
     }
   ]
   ```

2. GET /tests/statistics - для получения статистики

   ```shell
   curl --header "content-type:application/json" \
       --request GET http://0.0.0.0:9000/tests/statistics/
   ```

   ```json
   [
     {
       "species": "коза",
       "total_tests": 1,
       "avg_milk_yield": 3.2,
       "max_milk_yield": 3.2,
       "good_health_percentage": 100.0
     },
     {
       "species": "корова",
       "total_tests": 2,
       "avg_milk_yield": 30.25,
       "max_milk_yield": 32.0,
       "good_health_percentage": 100.0
     },
     {
       "species": "теленок",
       "total_tests": 2,
       "avg_milk_yield": 0.0,
       "max_milk_yield": 0.0,
       "good_health_percentage": 50.0
     },
     {
       "species": "овца",
       "total_tests": 1,
       "avg_milk_yield": 0.0,
       "max_milk_yield": 0.0,
       "good_health_percentage": 100.0
     }
   ]
   ```
