# Rest service + docker

Список команд для запуска:

Запуск RestAPI application:
```PATH_TO_MODEL=models/model.pkl uvicorn app:app```

Запрос к приложению с предсказанием модели: 
```python -m src.make_request```

Тесты:
```pytest tests```

Docker build: 
```docker build -t balan/online_inference:v1 .```

Docker run: 
```docker run -p 8000:8000 balan/online_inference:v1```

Docker pull: 
```docker pull balan/online_inference:v1```


