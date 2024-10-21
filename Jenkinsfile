pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/omarzaki222/Realproject.git', branch: 'main'
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook playbook: 'ansible-playbook.yml', // Adjust this path if necessary
                                    inventory: 'ansible/inventory.ini', // Adjust this path if necessary
                                    extras: '--extra-vars "var1=value1"' // Pass any extra variables here
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
