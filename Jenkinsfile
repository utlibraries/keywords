pipeline {
  agent       { label 'linux' }
  options     {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    timestamps()
  }
  triggers    { cron('@weekly') }
  environment {
    CI = 'true'
    CONTAINER = 'prometheus'
  }
  stages {
    stage('Build') {
      steps {
        script {
          props = readProperties file: "./version"
          image = docker.build("utexas-glib-it-docker-local.jfrog.io/${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER}", "--pull ./ ")
        }
      }
    }
    stage('Test') {
      steps {
        script {
          sh "export GOSS_FILES_STRATEGY=cp; \
              GOSS_PATH='/usr/local/bin/goss' \
              GOSS_OPTS='--format junit --no-color' \
              GOSS_SLEEP='15' \
              /usr/local/bin/dgoss run \
              utexas-glib-it-docker-local.jfrog.io/${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER} \
                | grep -v INFO | grep -v UID > ./goss.xml"
          step([$class: 'JUnitResultArchiver', testResults: 'goss.xml'])
        }
      }
    }
  }
  post {
    always {
       deleteDir()
    }
    success {
      script {
        image.push()
        image.push("${props.MAJOR}.${props.MINOR}.${props.HOTFIX}")
        image.push("${props.MAJOR}.${props.MINOR}")
        image.push("${props.MAJOR}")
        image.push('latest')
      }
      slackSend message: "${currentBuild.currentResult}: ${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    }
    failure {
      slackSend message: "${currentBuild.currentResult}: ${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    }
    unstable {
      slackSend message: "${currentBuild.currentResult}: ${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    }
    changed {
      slackSend message: "${currentBuild.currentResult}: ${props.NAME}-${props.RELEASE}:${props.MAJOR}.${props.MINOR}.${props.HOTFIX}-${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    }
  }
}
