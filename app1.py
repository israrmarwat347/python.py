pipeline {
    agent any

    environment {
      // Your GitHub repository URL
        GIT_REPO = 'https://github.com/israrmarwat347/python.py.git'
        BRANCH = 'master' // Use the correct branch name where your Python script is located
    }

    stages {
        stage('Checkout Git') {
            steps {
                script {
                    // Checkout the repository from GitHub
                    git branch: "${BRANCH}", url: "${GIT_REPO}"
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Ensure Python is installed on your Jenkins machine
                    sh 'python3 app.py'  // Adjust path if needed, for example, './app.py'
                }
            }
        }
    }
}

