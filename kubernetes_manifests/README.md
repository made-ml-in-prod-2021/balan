# Homework 4: Kubernetes

## Description

Кластер был развернут с помощью Kubernetes Engine на платформе Google Cloud Platform

Информация о кластере: 
```bash
kubectl cluster-info
```

Деплой приложения на кластере через манифест:
```bash
kubectl apply -f online-inference-pod.yaml
```

Состояние подов на кластере:
```bash
kubectl get pods
```

Пробросить порт к поду для доступа по локальному адресу (127.0.0.1:8000):
```bash
kubectl port-forward pod/online-inference 8000:8000
```

Скриншоты с результатами успешного запуска можно найти в папке `screenshots`.

### Resources

Манифест `...-resources.yaml` содержит ограничения requests/limits:
- requests - кол-во ресурсов, которые будут обязательно предоставлены приложению
- limits - максимальное кол-во ресурсов для данного приложения

Эти указания полезны для оптимального распределения ресурсов между приложениями на кластере.

### Probes

Манифест `...-probes.yaml` содержит статусы readiness/liveness:
- readiness - управление временем готовности приложения для принятия запросов
- liveness - управление временем работы приложения, проверка работоспособности

## Evaluation

0) [0/0] Установите kubectl
1) [5/5] Разверните kubernetes  
Вы можете развернуть его в облаке:
- https://cloud.google.com/kubernetes-engine
- https://mcs.mail.ru/containers/
- https://cloud.yandex.ru/services/managed-kubernetes
Либо воспользоваться локальной инсталляцией
- https://kind.sigs.k8s.io/docs/user/quick-start/
- https://minikube.sigs.k8s.io/docs/start/

Напишите, какой способ вы избрали. 
Убедитесь, с кластер поднялся (kubectl cluster-info) 
(5 баллов)

2) [4/4] Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml (https://kubernetes.io/docs/concepts/workloads/pods/)
Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods)
Приложите скриншот, где видно, что все поднялось
(4 балла)

2а) [2/2] Пропишите requests/limits и напишите зачем это нужно в описание PR
закоммитьте файл online-inference-pod-resources.yaml
(2 балл)

3) [3/3] Модифицируйте свое приложение так, чтобы оно стартовало не сразу(с задержкой секунд 20-30) и падало спустя минуты работы. 
Добавьте liveness и readiness пробы , посмотрите что будет происходить.
Напишите в описании -- чего вы этим добились.

Закоммититьте отдельный манифест online-inference-pod-probes.yaml (и изменение кода приложения)
(3 балла)

Получилось баллов: 14