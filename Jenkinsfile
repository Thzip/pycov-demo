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
            post{
                failure {
                    emailext body: '模块${source_code_need_code_coverage_check}单元测试覆盖率不足${code_coverage_threshold}，详细查看构建日志${absoluteUrl}', subject: '单元测试覆盖率不足', to: 'huawei.yang@ecarx.com'
                }
            }
        }
    }
}
