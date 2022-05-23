pipeline {

        stage("docker compose up") {

            steps {

                script {
                            dir('final/') {
                                sh "docker-compose up --abort-on-container-exit"
                            }

                }
            }
        }

        stage("Closing and deleting infrastructure") {
            steps {


                    dir('TEST_FRAMEWORK/final-project') {
                        sh "docker-compose down -v"


                        }

            }
        }
    }
