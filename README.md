# Django
Django




Запрос API GET к сущностям  ***product*** ***category*** ***orderitem*** ***order***
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

