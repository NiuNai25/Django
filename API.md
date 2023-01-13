 
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

