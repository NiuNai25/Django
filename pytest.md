# Django

В папке /myshop/tests находится файл test_API.py в котором реализованно тестирование API через pytest

Файл содержит три функции для тесторивания обращения к Категориям приложения.
Тест выполненен при условии возвращения ответа status_code 201, 204 или 200


Для запуска необходимо запустить в терминале следующую команду: 

 ```
 pytest tests/test_API.py
 ```
**Обновление категории**

``` python 
def test_category_update():
    n = 3 #id категории
    category = {"name": "Wine","slug": "wine"}
    url = ('http://drytova:qwerty@127.0.0.1:8000/api/category/'+str(n)+'/update/')
    r = requests.put(url, json=  category )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]  
```

**Добавление категории**

``` python 
def test_category_add():
    category = {"name": "Gin_","slug": "gin"}
    url = 'http://drytova:qwerty@127.0.0.1:8000/api/category/1/add/'
    r = requests.post(url, json=  category )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]
```

**Удаление категории**


``` python 
def test_category_del():
    n = 19 #id категории
    url = ('http://drytova:qwerty@127.0.0.1:8000/api/category/'+str(n)+'/delete/')
    r = requests.delete(url)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]    
```
