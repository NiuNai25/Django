
## Тестирование отдельных Юнитов

В качестве примера тестирования отдельных Юнитов, реализованно тестирование полей model.py каталога orders:


```python
class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Order.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'Имя')

    def test_email(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')
```

Для тестования необходимо запустить приложение и запустить в терминате команду

```
python manage.py test
```
