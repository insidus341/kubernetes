pipeline {
    environment{
        registry = "insidus341/nginx-custom"
        registryCredential = "DockerHub"
        main_branch = "main"
        development_branch = "development"
    }

    agent any

    stages {  
        stage('Build Docker Image') {
            when {
                expression {
                    (env.CHANGE_ID && env.BRANCH_NAME.startsWith("PR-")) || env.BRANCH_NAME == development_branch || env.BRANCH_NAME == main_branch
                }
            }

            steps {
                script {
                    dockerImage = docker.build("nginx-custom", "./docker/nginx-test") registry + ":beta-$BUILD_NUMBER"
                }
            }
        }

        // stage ('Push container to Docker Hub') {
        //     when {
        //         expression {
        //             env.BRANCH_NAME == development_branch || env.BRANCH_NAME == main_branch
        //         }
        //     }

        //     steps {
        //         script {
        //             if (env.BRANCH_NAME == development_branch) {
        //                 docker.withRegistry('', registryCredential) {
        //                     dockerImage.push("beta-$BUILD_NUMBER")
        //                     dockerImage.push("beta")
        //                 }
        //             }

        //             if (env.BRANCH_NAME == main_branch) {
        //                 docker.withRegistry('', registryCredential) {
        //                     dockerImage.push("$BUILD_NUMBER")
        //                     dockerImage.push("latest")
        //                 }
        //             }
        //         }
        //     }
        // }
    }
}
