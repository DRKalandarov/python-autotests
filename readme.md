#### Сборка и запуск контейнеров в фоновом режиме.

---

```commandline
docker-compose up -d
```
Jenkins будет доступен по адресу `http://localhost:8080`, сервер на FastAPI - `http://localhost:8000`

#### Первоначальная настройка Jenkins.

---

1. Получить пароль администратора: `cat /var/lib/jenkins/secrets/initialAdminPassword`
2. Установить рекомендуемые плагины, выбрав "Install suggested plugins".
3. Создать пользователя (можно пропустить - "Skip and continue as admin").
4. Перейти на главную страницу, нажав на "Start using Jenkins".
5. Установить плагины Allure и HTML Publisher (Настроить Jenkins -> Plugins -> Available plugins).
6. Установить Allure Commandline (Настроить Jenkins -> Tools -> Добавить Allure Commandline).
7. Добавить файл с тестовым окружением (Настроить Jenkins -> Credentials -> Global credentials -> Add credentials):
    - Kind - Secret file.
    - Scope - Global.
    - ID - LOCAL.
8. При создании пайплайна добавить два строковых параметра:
    - BRANCH_NAME (дефолтное значение - main).
    - ENV_NAME (дефолтное значение - LOCAL).