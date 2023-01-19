Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages{
        stage('Check'){
            steps{
                script{
                    env.tyt = ''
                    try{
                    sh 'sudo -u hdoop jps | grep NodeManager'
                    }
                    catch(Exception e){
                        env.tyt = env.tyt + "NodeManager"
                    }
                    if (env.tyt != ''){
                        sh 'false'
                    }
                }
            }
        }
        stage('Nginx'){
            steps{
                sh 'ansible-playbook ./techtask/ansible/play.yml'
            }
        }
    }
    post{
        failure{
            echo "$tyt not working"
        }
    }
}
