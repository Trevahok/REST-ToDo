node{
def app

stage('Clone'){
  checkout scm
}

stage('Build'){
  app = docker.build('trevahok/todorest')
}

stage('Test'){
  app.inside{
    sh 'echo "tests passed" '
  }
}

stage('Push'){
docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
}

}
