pipeline {
        agent any
        stages {

                stage("docker compose up") {

                steps {

                        script {
                            dir('final/') {
                                sh "docker-compose up --abort-on-container-exit"
                            }

                }
            }
        }

        stage("docker compose down") {
            steps {

                    script {
                    dir('final/') {
                        sh "docker-compose down -v"


                        }

            }
        }
    }
 }
}
