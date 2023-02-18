# blog
# Платформа для ведения пользовательских блогов "Yatube"
### Описание
###### Пользователь может:
- писать посты, редактировать их и загружать картинки
- комментировать посты
- подписываться на авторов
- зарегестрироваться и авторизоваться
- просматривать страницы групп
### Технологии
Python 3.7
Django 2.2.19

### Локальный запуск в Docker
- Установите Docker
- В папке c Dockerfile выполните команду сборки образа
docker build -t blog:v1 .
- Проверьте образ
```
docker image ls
```
- Запустите контейнер
```
docker run --name web -it -p 8000:8000 akcaau/blog:latest
```
- Проверьте контейнер
```
docker container ls
```


### Локальный запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
###### Автор - Глеб Лазарев, 2022

Примеры запросов
1. Запрос к постам
[GET, POST] http://127.0.0.1:8000/api/v1/posts/

Response
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
2. Запрос к посту
[GET, PULL, PATCH, DELETE] http://127.0.0.1:8000/api/v1/posts/{id}/

Response
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
3. Запрос к комментариям поста
[GET, POST] http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Response
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
4. Подписка на автора
[GET, POST] http://127.0.0.1:8000/api/v1/follow/

Response
{
    "following": "string"
}
