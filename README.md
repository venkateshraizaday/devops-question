# devops-question
Skeleton setup for devops hiring question

### The Question
#### Write a script that does the following
* Checkout code from https://github.com/venkateshraizaday/devops-question.git
* Build code via `scripts/ci.sh` command.
* Copy contents from build folder to another folder location outside of git folder
* Change app folder ownership
* Run app via `app/scripts/run.sh`

### Interviewer notes (Not to be shared with interviewee until needed)
* Since files are not getting copied over to a remote server just ask in theory on how to copy files from one server to another.
* Bash tip: `scp` is a standard command to copy files across servers.
* Bash tip: Use `chown 755` for permission modification.
* Bash Solution:
        
        
        # clone
        git clone https://github.com/venkateshraizaday/devops-question.git

        # build
        cd devops-question
        chmod 755 scripts/ci.sh
        ./scripts/ci.sh

        # deploy
        cd ..
        mkdir app
        cp -R devops-question/build/* app/
        chmod -R 755 app

        # run
        cd app
        ./scripts/run.sh