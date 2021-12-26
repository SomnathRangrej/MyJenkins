- Exercise files: https://github.com/LinkedInLearning/learning-jenkins-3003221/tree/main

- Contents:
  - Introduction to Jenkins
  ![Jenkins Dashboard](/Jenkins/Learning_Jenkins/Jenkins_Dashboard.jpg)
  - Install Jenkins
    - If you are running Jenkins as a Docker Container, what is the minimum RAM you will need?
        - 1 GB
    - Jobs in Jenkins
      - Job types
        - You need to create a job that requires a series of steps to produce a final outcome. Which type of job is best to select?
        - Pipeline
      - Buid triggers
        - You want to trigger a job on a schedule. Which option under the Build Triggers section in Jenkins should you select?
        - Build periodically
      - Build environment
        - Why would you want to discard old builds?
        - to free up space on your server
        - Within the build environment section of Jenkins, where can you aggregate downstream test results?
        - under Post-build Actions
      - More details on Job:
        - Global build tools
          - Giving path for local Git
          - Configuring Maven
          - Configuring JDK
          - Managing Artifacts
          - Parameters & Environment variables
          - Schedule jobs
      - Organise jobs with views & folders
        - Views are just like filters
        - Folders: for proper organsiation of jobs
          - When you delete a folder, what happens to the contents of that folder?
          - All the contents of the folder are deleted, along with the folder.
      - Pipeline as code
        - Create a pipeline job.
        - Paste the following code in the pipeline definition:
        - Pipeline consist of many stages, each stage consist of at least 1 step
        ```
        pipeline {
            agent any
            options {
                buildDiscarder(logRotator(daysToKeepStr: '10', numToKeepStr: '10'))
                timeout(time: 12, unit: 'HOURS')
                timestamps()
            }
            triggers {
                cron '@midnight'
            }
            stages {
                stage('Initialize') {
                    steps {
                        echo 'Initializing..'
                    }
                }
                stage('Build') {
                    steps {
                        echo 'Building..'
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing..'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying....'
                    }
                }
            }
        }
        ```
    ![Pipeline job output on console](/Jenkins/Learning_Jenkins/Pipeline_job_output.jpg)
