Побежимов Александр

Тестовое задание на Python

Cервис с использованием django, django-rest-framework, peewee и PostgreSQL, который принимает и отвечает на HTTP запросы.

### Порядок установки и запуска

**Создать виртуальное окружение и установить зависимости**

    mkdir test_project
    cd test_project
    python3 -m venv venv
    ./venv/Scripts/activate
    pip install django djangorestframework peewee peewee-validates psycopg2

**Установить PostgreSQL**

После установки в SQL Shell создать базу данных:

    CREATE DATABASE firecode_test    
 
**Клонировать проект**

**Выполнить окончательные действия**

    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata whole.json
    python3 manage.py createsuperuser

####Запуск сервера

    python manage.py runserver

### Порядок работы

Начальные данные были загружены в БД на этапе установки. Добавить данные можно через панель администратора Django:

http://localhost:8000/admin

Точка входа API:

http://localhost:8000/api

Методы:

GET /city/ - получение всех городов из базы; 

GET /city/street/ - получение всех улиц; 

GET /city/street/?city_id= - получение всех улиц указанного города (city_id - идентификатор города)  

POST /shop/ - создание магазина; Данный метод получает json c 
объектом магазина, в ответ возвращает id созданной записи.  

GET /shop/?street=&city=&open=0/1 — получение списка магазинов (street - идентификатор улицы, city - идентификатор города, open - открыт или закрыт в текущий момент времени (0-закрыт, 1-открыт))