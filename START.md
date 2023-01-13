

## **Запуска приложения:**
1. Установите рабочую дерикторию django/myshop

1.1. Убедитесть что файл django/myshop/myshop/settings.py имеет следующие параметры:
```
SECRET_KEY = 'cb7)kfkzv6x#livk_^2o$c_r9-we-6v6s=#89i)i4^1e=^!&4^'
DEBUG = True
ALLOWED_HOSTS = []
```
1.2 Запустите в терминате
````
python manage.py runserver

````
1.3 Откройте в браузере http://127.0.0.1:8000/
 

ИЛИ

2. Установите рабочую дерикторию django/myshop

2.1. Убедитесть что файл django/myshop/myshop/settings.py имеет следующие параметры:
```
SECRET_KEY = environ.get('SECRET_KEY')
DEBUG = int(environ.get('DEBUG', default=0))
ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(' ')
```
2.2 Убедитесь что приложение Docker запущенно и запустите следующую команду в терминале 
```
docker-compose up -d
```
2.3 Откройте в браузере http://localhost:8000/

