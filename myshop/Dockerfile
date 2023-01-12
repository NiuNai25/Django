# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.8
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR 'C:\Users\drytova\OneDrive - Reckitt\Desktop\HomeWork\django\myshop'
# Копирует все файлы из нашего локального проекта в контейнер

# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY ./ ./
EXPOSE 8000
CMD ['python', './manage.py','runserver','0.0.0.0:8000']

