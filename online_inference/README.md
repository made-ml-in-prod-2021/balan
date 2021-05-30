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

```docker build -t ooptyp/online_inference:v1 .```
```docker run -p 8000:8000 ooptyp/online_inference:v1```

Образ опубликован на dockerhub: https://hub.docker.com/r/ooptyp/online_inference

```docker pull balan/online_inference:v1```

Удалось добиться уменьшения размера docker image засчёт выбора версии python: 
- 1.3 GB - python:3.8
- 600 MB - python:3.8-slim
