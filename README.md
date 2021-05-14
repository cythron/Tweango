## Patch  Action

Since the vulnerability stays on any further commit, due to commit history, it must be patched from your side to mitigate completely.

It is recommended to overwrite history in the remote repo.

       1. rm -rf .git 
       2. git init
       3. git add .
       4. git commit -m 'new commit'
       5. git remote add origin <github-uri>
       6. git push -u --force origin master

Please visit <a href = 'https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository/13102849#13102849'>StackOverflow Solution </a>, if any issue.
This is what can be done to patch from my side. 

### P.S.: Please remove this `README.md` file gefore `git add  .`
