pipeline {
        agent any
        stages {

                stage("docker compose up") {

                steps {

                        script {
                            dir('final/') {
                                bat "docker-compose up --abort-on-container-exit"
                            }

                }
            }
        }

        stage("docker compose down") {
            steps {

                    script {
                    dir('final/') {
                        bat "docker-compose down -v"


                        }

            }
        }
    }
 }
}
