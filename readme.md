Создание Docker-образа:
```commandline
docker build -t my-jenkins-python .
```
Запуск контейнера:
```commandline
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v ~/jenkins_home:/var/jenkins_home my-jenkins-python
```
Остановка контейнера:
```commandline
docker stop jenkins
```
Удаление контейнера после остановки:
```commandline
docker rm jenkins
```
---
Генерация allure отчета:
```commandline
allure generate ./tests/resources/report/allure/results --clean -o ./tests/resources/report/allure/report
```