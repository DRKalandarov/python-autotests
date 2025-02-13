pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                // Очистка рабочего пространства
                cleanWs()
            }
        }
        stage('Checkout branch') {
            steps {
                git branch: "${BRANCH_NAME}", url: 'https://github.com/Calandarov/python-autotests.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Создаем и активируем виртуальное окружение, устанавливаем зависимости
                sh """
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }
        stage('Load .env') {
            steps {
                script {
                    // Создаем файл .env
                    withCredentials([file(credentialsId: "${ENV_NAME}", variable: 'ENV')]) {
                        def envContent = readFile(ENV)
                        writeFile file: '.env', text: envContent
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Запускаем тесты в виртуальном окружении
                sh """
                    . ${VENV_DIR}/bin/activate
                    mkdir -p "tests/resources/logs"
                    touch "tests/resources/logs/debug.log"
                    pytest tests/api/test_jsonplaceholder --env=.env
                """
            }
        }
    }

    post {
        always {
            stage('Publish Allure Report') {
                steps {
                    // Публикация отчета Allure
                    allure includeProperties: true,
                        jdk: '',
                        properties: [],
                        results: [[path: 'tests/resources/report/allure/results']],
                        report: 'tests/resources/report/allure/report'
                }
            }
            stage('Publish HTML Report') {
                steps {
                    // Публикация отчета pytest_html
                    publishHTML([
                        alwaysLinkToLastBuild: true,
                        allowMissing: false,
                        keepAll: true,
                        reportDir: 'tests/resources/report/pytest_html',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report',
                        reportTitles: ''
                    ])
                }
            }
            echo 'Pipeline завершен.'
        }
        success {
            echo 'Тесты прошли успешно!'
        }
        failure {
            echo 'Тесты не прошли.'
        }
    }
}