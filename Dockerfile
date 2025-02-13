# Базовый образ Jenkins
FROM jenkins/jenkins:lts

# Запускаем от root, чтобы установить пакеты
USER root

# Устанавливаем Python, pip и необходимые утилиты
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv wget unzip openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Allure Commandline
RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.zip -O allure.zip && \
    unzip allure.zip -d /opt/ && \
    rm allure.zip && \
    ln -s /opt/allure-2.32.2/bin/allure /usr/bin/allure

# Указываем рабочую директорию Jenkins
USER jenkins

# Устанавливаем рабочую директорию для Jenkins
WORKDIR /var/jenkins_home
