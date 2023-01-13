# Django
Django
Проект веб приложения ИНТЕРНЕТ - МАГАЗИН :shipit:

## **Запуска приложения:**

[a relative link](other_file.md)


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

##  **Структура приложения**
 
 <table>
  <tr>
    <td>PRODUCT</td>
    <td>PRODUCT DETAILS </td>
    <td>CART</td>
    <td>ORDER</td>
    <td>ORDER ID</td>
  </tr>
 
  <tr>
  <td><img src=https://user-images.githubusercontent.com/117024752/212306277-b1c602d7-532c-4f5f-8ca9-4c26a2cb0537.png width=200 height=150></td>
 <td><img src=https://user-images.githubusercontent.com/117024752/212307367-22a68f40-cad8-452e-a11c-0966a0779a35.png width=200 height=150></td>
 <td><img src=https://user-images.githubusercontent.com/117024752/212308838-74c008a3-e255-4df8-a584-40fd1c108668.png width=200 height=150></td>
 <td><img src=https://user-images.githubusercontent.com/117024752/212309409-616ef878-a561-4758-9ccc-03f02286036c.png width=200 height=150></td>
 <td><img src=https://user-images.githubusercontent.com/117024752/212309533-72c269ff-e537-47cc-a52f-eba167a84218.png width=200 height=150></td>
</tr>
   </table>
 
##  **Запрос API**

 1.GET к сущностям  ***product, category, orderitem, order***
 
``` python
import requests
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('admin', 'admin')
view = 'product' #View
url = "http://127.0.0.1:8000/api/"+view+"/"
resp = requests.get(url, auth = basic)
print(resp.status_code)
print(resp.text)
```


 2.PUT к сущностям  ***product, category***

``` python
import requests
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('admin', 'admin')
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
view = 'category'
id = 1
url = "http://127.0.0.1:8000/api/"+view+"/"+str(id)+"/update/"
data = """
{
    "name": "Чай",
    "slug": "tea"
    }
"""
resp = requests.put(url, auth = basic,  headers= headers, data = data)
print(resp.status_code)
print(resp.text)
```

3.POST к сущностям ***category***

``` python
import requests
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('admin', 'admin')
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
view = 'category'
id = 1
url = "http://127.0.0.1:8000/api/"+view+"/"+str(id)+"/add/"
data = """
{
    "name": "Gin",
    "slug": "gin"
}
"""
resp = requests.post(url, auth = basic,  headers= headers, data = data)
print(resp.status_code)
print(resp.text)
```
4.DELETE к сущностям ***order, category***
```python
import requests
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth


basic = HTTPBasicAuth('admin', 'admin')

view = 'category'
id = 19

url = "http://127.0.0.1:8000/api/"+view+"/"+str(id)+"/delete/"
resp = requests.delete(url, auth = basic,  headers= headers)

print(resp.status_code)
print(resp.text)
```
