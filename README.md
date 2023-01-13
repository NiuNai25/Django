# Django
Django
Проект веб приложения ИНТЕРНЕТ - МАГАЗИН

Product

 <img src=https://user-images.githubusercontent.com/117024752/212306277-b1c602d7-532c-4f5f-8ca9-4c26a2cb0537.png width=450 height=450>
 
Product details

 <img src=https://user-images.githubusercontent.com/117024752/212307367-22a68f40-cad8-452e-a11c-0966a0779a35.png width=450 height=450>


Cart

<img src=https://user-images.githubusercontent.com/117024752/212308838-74c008a3-e255-4df8-a584-40fd1c108668.png width=450 height=450>


Order 

 <img src=https://user-images.githubusercontent.com/117024752/212309409-616ef878-a561-4758-9ccc-03f02286036c.png width=450 height=450>


Order id

 <img src=https://user-images.githubusercontent.com/117024752/212309533-72c269ff-e537-47cc-a52f-eba167a84218.png width=450 height=450>



Запрос API

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
