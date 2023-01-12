import pytest
import requests



@pytest.mark.django_db()
def test_category_update():
    n = 12 #id категории
    category = {"name": "Gin","slug": "gin"}
    url = ('http://drytova:qwerty@127.0.0.1:8000/api/category/'+str(n)+'/update/')
    r = requests.put(url, json=  category )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]    


def test_category_del():
    n = 17 #id категории
    url = ('http://drytova:qwerty@127.0.0.1:8000/api/category/'+str(n)+'/delete/')
    r = requests.delete(url)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]
    


def test_category_add():
    category = {"name": "Gin_","slug": "gin"}
    url = 'http://drytova:qwerty@127.0.0.1:8000/api/category/1/add/'
    r = requests.post(url, json=  category )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code in [201,204,200]
    
