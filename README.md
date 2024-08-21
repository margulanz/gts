# Installation

1) `git clone https://github.com/margulanz/gts.git`
2) `cd gts`
3) `docker compose up --build`
4) Откройте Docker Desktop и зайдите в терминал контейнера `gts-admin_backend-1`
5) `python manage.py createsuperuser` для создания админ аккаунта
6) В браузере откройте http://localhost:8000/admin/ и войдите в админ аккаунт
7) Создайте Теги в Tags
8) Создайте категорию в Categorys


# Функционал
1) Для реализации авторизации использовалась библиотека dj_rest_auth
2) При помощи docker compose запускается 2 Django приложения (админ и пользователь) и БД (postgresql)
3) Реализован автоматический Slug. Так же можно его задать вручную
4) Реализован поиск по ключевым словам, тегам и категориям
5) Для каждого из приложений были созданы отдельные пользователи Postgres. Для админ приложения был создан admin_user, с полным доступом к БД. Для пользовательского приложения был создан reader_user, с доступом только к чтению БД


# API
## Для админа
- `http://localhost:8000/auth/registration/` (POST) - Регистрация дла админов
- `http://localhost:8000/auth/login/` (POST) - авторизация админов. Возвращает токен. Для создание новостных постов обязательно нужно авторизоваться. Без авторизации можно будет только читать новости
- `http://localhost:8000/news/` (GET) - возвращает список всех новостей
- `http://localhost:8000/news/` (POST) - создание новостного поста (админ обязательно должен быть авторизован в системе)
- `http://localhost:8000/news/<slug>/` (GET) - возвращает новостной пост
- `http://localhost:8000/news/<slug>/` (PUT, PATCH) - редактирует существующий новостной пост
- `http://localhost:8000/news/<slug>/` (DELETE) - удаляет новостной пост
- `http://localhost:8000/news/?tags=some-tag` (GET) - поиск по тегам. возвращает список ссылок на новость
- `http://localhost:8000/news/?category=some-category` (GET) - поиск по категориям. возвращает список ссылок на новость
- `http://localhost:8000/news/?keywords=some-words` (GET) - поиск по ключевым словам. возвращает список ссылок на новость

## Для пользователей
- `http://localhost:8080/news/` (GET) - возвращает список всех новосте
- `http://localhost:8080/news/<slug>/` (GET) - возвращает новостной пост
- `http://localhost:8080/news/?tags=some-tag` (GET) - поиск по тегам. возвращает список ссылок на новость
- `http://localhost:8080/news/?category=some-category` (GET) - поиск по категориям. возвращает список ссылок на новость
- `http://localhost:8080/news/?keywords=some-words` (GET) - поиск по ключевым словам. возвращает список ссылок на новость