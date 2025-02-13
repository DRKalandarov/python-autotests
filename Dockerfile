# Базовый образ Jenkins
FROM jenkins/jenkins:lts

# Запускаем от root, чтобы установить пакеты
USER root

# Устанавливаем Python и pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Указываем рабочую директорию Jenkins
USER jenkins