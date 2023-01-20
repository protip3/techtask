pipeline {
    agent any
    stages{
        stage('Check'){
            steps{
                script{
                    env.faildserv = ''
                    try{
                    sh 'sudo -u hdoop jps | grep NodeManager'
                    }
                    catch(Exception e){
                        env.faildserv = env.faildserv + "NodeManager "
                    }
                    try{
                        sh 'ps -ef | grep hadoop | grep -P  "datanode"'
                    }
                    catch(Exception e){
                        env.faildserv = env.faildserv + "DataNode "
                    }
                    try{
                        sh 'ps ww -f -C java | grep resourcemanager'
                    }
                    catch(Exception e){
                        env.faildserv = env.faildserv + "ResourceManager"
                    }
                    if (env.faildserv != ''){
                        sh 'false'
                    }
                }
            }
        }
        stage('Nginx'){
            steps{
                sh 'git clone https://github.com/protip3/techtask.git'
                sh 'ansible-playbook ./techtask/ansible/play.yml'
                sh 'curl localhost:80'
            }
        }
    }
    post{
        always {
            cleanWs()
        }
        failure{
            echo "$faildserv not working"
        }
    }
}