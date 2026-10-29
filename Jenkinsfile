pipeline {
  agent any
  environment {
    IMAGE     = 'pavankv5/expense-app'
    TAG       = "build-${env.BUILD_NUMBER}"
    NAMESPACE = 'expense-system'
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build image') {
      steps { sh 'docker build -t $IMAGE:$TAG app/' }
    }
    stage('Push image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                         usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh '''
            echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
            docker push $IMAGE:$TAG
            docker logout
          '''
        }
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([
          string(credentialsId: 'expense-db-password', variable: 'DB_PASS'),
          string(credentialsId: 'django-secret-key', variable: 'DJANGO_KEY')
        ]) {
          sh '''
            helm upgrade --install expense-app expense-app-chart \
              -n $NAMESPACE --reuse-values \
              --set image.tag=$TAG \
              --set database.password="$DB_PASS" \
              --set-string djangoSecretKey="$DJANGO_KEY" \
              --wait --timeout 5m
          '''
        }
      }
    }
    stage('Verify') {
      steps {
        sh '''
          kubectl rollout status deployment/expense-app -n $NAMESPACE --timeout=120s
          kubectl get pods -n $NAMESPACE
        '''
      }
    }
  }
}
