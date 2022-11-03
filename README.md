# devops-question
Skeleton setup for devops hiring question

### The Question
#### Write a script that does the following
* Checkout code from https://github.com/venkateshraizaday/devops-question.git
* Build code via script/ci.sh command.
* Copy contents from build folder to remote server
* Change app folder ownership
* Run app via app/scripts/run.sh

### Interviewer notes (Not to be shared with interviewee until needed)
* Use chown 755 for permission modification.
* Heroku VM can be used for providing remote server.
