- Port number on which Jenkins runs: http://localhost:8080/ 
- ID: Admin
- Name: SOMNATH RANGREJ
- Email: rangrejsomnath19@gmail.com
- Pass: 

- How to run Jenkins on my machine locally:
  - E:\Soft>java -jar jenkins.war
  - Jenkins is fully up and running
	 
- How & where to specify location Git location in Jenkins [one time operation for first run]?
	- On home page -> Manage Jenkins-> Global tool Configuration -> Under "Git" tab -> Path to git executable
	- C:\Program Files\Git\bin\git.exe
	- Apply
	- Save
	
- How to setup a project & run the job?
	- New item
	- Enter name of item
	- Category -> Select "Freestyle project"
	- Under tab "Source Code Management" -> Git -> Enter repository URL
	- Branch specifier: Master or Main whichever is True for your case
	- Scroll down -> Build tab -> Execute Window batch command
	- Give actual commad or Run.bat if kept at root location of project

- You can run Jenkins as docker container:
	Installation
	In a terminal, run the following commands:

	docker --version

	docker pull jenkins/jenkins:lts  # To pull jenkins image on your local machine

	docker run --detach --publish 8080:8080 --volume jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts   # To run jenkins as container

	docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword   # To get initial password printed on screen

	

	