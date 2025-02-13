pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
//         ENV_FILE = credentials('554ec798-c033-48ed-861c-e2e3b0206493')
    }

    stages {
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
        stage('Cleanup') {
            steps {
                script {
                    sh 'rm -f .env* .env'
                }
            }
        }
        stage('Load .env') {
            steps {
                script {
                    // Создаем файл .env
                    def envContent = """
                    JSONPLACEHOLDER_HOST='https://jsonplaceholder.typicode.com'
                    LOCALHOST=${credentials('LOCALHOST')}
                    """
                    writeFile file: '.env.local', text: envContent
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
                    pytest tests/api/test_jsonplaceholder
                """
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Генерация HTML-отчета Allure
                sh 'allure generate tests/resources/report/allure/results -o tests/resources/report/allure --clean'
            }
        }
        stage('Publish Allure Report') {
            steps {
                // Публикация отчета Allure
                allure([
                    reportDir: 'tests/resources/report/allure',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
//         stage('Publish HTML Report') {
//             steps {
//                 // Публикация отчета pytest_html
//                 publishHTML(target: [
//                     reportName: 'Test Report',
//                     reportDir: 'tests/resources/report/pytest_html',
//                     reportFiles: 'report.html',
//                     alwaysLinkToLastBuild: true,
//                     keepAll: true
//                 ])
//             }
//         }
    }

    post {
        always {
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