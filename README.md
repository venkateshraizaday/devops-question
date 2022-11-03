# devops-question
Skeleton setup for devops hiring question

<h5>The Question: Write a script that does the following</h5>
- Checkout code from https://github.com/venkateshraizaday/devops-question.git
- Build code via script/ci.sh command.
- Copy contents from build folder to remote jenkins@192.168.12.2/app (Assume connectivity/permissions are already setup)
- Change app folder ownership (Hint use chown -R 755 app)
- Run app via app/scripts/run.sh