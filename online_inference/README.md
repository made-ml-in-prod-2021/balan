# Rest service + Docker

Ниже представлен список команд для запуска

Запуск RestAPI application:

```PATH_TO_MODEL=models/model.pkl uvicorn app:app```

Запрос к приложению с предсказанием модели: 

```python -m src.make_api_request```

Тестирование:

```pytest tests```

## Docker

Build + run:

```
docker build -t ooptyp/online_inference:v1 .
docker run -p 8000:8000 ooptyp/online_inference:v1
```

Образ опубликован на dockerhub: https://hub.docker.com/r/ooptyp/online_inference

```docker pull balan/online_inference:v1```

Удалось добиться уменьшения размера docker image засчёт выбора версии python: 
- 1.3 GB - python:3.8
- 600 MB - python:3.8-slim


## Прогресс

Ниже обозначены проделанные пункты:

[+0/0] ветку назовите homework2, положите код в папку online_inference

[+3/3] Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict (3 балла)

[+3/3] Напишите тест для /predict (3 балла) (https://fastapi.tiangolo.com/tutorial/testing/, https://flask.palletsprojects.com/en/1.1.x/testing/)

[+2/2] Напишите скрипт, который будет делать запросы к вашему сервису -- 2 балла

[+3/3] Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном, типы не те и пр, в рамках вашей фантазии) (вы можете сохранить вместе с моделью доп информацию, о структуре входных данных, если это нужно) -- 3 доп балла
https://fastapi.tiangolo.com/tutorial/handling-errors/ -- возращайте 400, в случае, если валидация не пройдена

[+4/4] Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4 балл)

[+3/3] Оптимизируйте размер docker image (3 доп балла) (опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться) -- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

[+2/2] опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) (2 балла)

[+1/1] напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1 балл)
Убедитесь, что вы можете протыкать его скриптом из пункта 3

[+1/1] проведите самооценку -- 1 доп балл

[✅] создайте пулл-реквест и поставьте label -- hw2

Получилось баллов: 22
