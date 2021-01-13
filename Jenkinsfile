pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/Thzip/pycov-demo.git'

				// Run test
                sh "pytest --cov-config=.coveragerc --cov=source --cov-report=xml:coverage.xml --cov-report=term --junit-xml=result.xml --alluredir=.allure"
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])

                    junit allowEmptyResults: true, testResults: 'result.xml'

                    allure includeProperties: false, jdk: '', results: [[path: '.allure']]
                }
            }

        }

    }
}
