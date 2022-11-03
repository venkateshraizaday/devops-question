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
        
Output:
        Cloning into 'devops-question'...
        remote: Enumerating objects: 29, done.
        remote: Counting objects: 100% (29/29), done.
        remote: Compressing objects: 100% (19/19), done.
        remote: Total 29 (delta 9), reused 23 (delta 5), pack-reused 0
        Receiving objects: 100% (29/29), done.
        Resolving deltas: 100% (9/9), done.
        Code loops to 1000 and prints numbers divisible by 7 and 11
        77
        154
        231
        308
        385
        462
        539
        616
        693
        770
        847
        924
