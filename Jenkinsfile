pipeline {
    agent any

    stages {
        stage('UnitTest') {
            steps {
                git 'https://github.com/Thzip/pycov-demo.git'
                sh "pytest --cov-config=.coveragerc --cov=${source_code_need_code_coverage_check} --cov-report=xml:coverage.xml --cov-report=term --junit-xml=result.xml --alluredir=.allure ${test_case_path}"
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

        stage('CodeCov Gate'){
            steps{
                sh "python3 covrate_gate.py -P ${source_code_need_code_coverage_check} -R ${code_coverage_threshold}"
            }
        }
    }
}
