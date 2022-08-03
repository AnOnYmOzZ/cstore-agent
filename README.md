# cstore-agent

# Steps: 
1. Clone git repo 
2. Install virtualenv 
3. Install ansible 
4. Work on the ansible file 
	a. Pull ansible tasks repo 
		SSH link: git@github.com:cliffordolaw/ansible-pull-sample-tak.git
		Https link: https://github.com/cliffordolaw/ansible-pull-sample-task.git

		Sample command: 
		sudo ansible-pull -U https://github.com/cliffordolaw/ansible-pull-sample-task.git
		
	b. Modify the ansible yaml file accordingly (hostname, list of tasks) 
	c. Push back to repo 
	
5. Modify the python app config file accordingly 
	a. ansible-pull command and the git repo to pull ansible yaml file from 
	b. endpoint for registering agent 
	
6. Update cron job "rc.local" to suit your application
