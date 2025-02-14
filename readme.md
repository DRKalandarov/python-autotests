Сборка и запуск контейнеров в фоновом режиме:
```commandline
docker-compose up -d
```
---
Генерация allure отчета:
```commandline
allure generate ./tests/resources/report/allure/results --clean -o ./tests/resources/report/allure/report
```