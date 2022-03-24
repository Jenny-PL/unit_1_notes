## Notes from TA session 3/10/22 with Goeun:

To add a commit:
- Step 1. Put in the staging area.
- Step 2. Commit.

**git status** — Information about the current state of the tracked files (do they need to move up to staging? do they need to be committed?)

**git add [file] or git add . for all files**— Step 1 of committing files in git. Changes that are added here move onto a staging area (fancy git term, don’t worry about it) but are not yet committed!

**git commit [file] or git commit . for all files** — Step 2 of committing files in git. This will open your VS code and request you to type in a commit message before closing.  
(Alternately:  **git commit -m "First commit!"**  allows you to add the commit msg in the terminal)

Now your changes are in your local git! You can check this by looking at your log via **git log** (press q to exit out of the view!)

**git push** — This pushes all your commits on your local machine onto your GitHub repository!

--- 
## Git collaboration steps:
When working with others, each person will have their own version of the repo (a clone) on their computer.  Steps to collaborating:
1. clone the origin repo (git clone https://...)
2. cd to repo_clone
3. work on repo_clone
4. Make a pull BEFORE you try to add your own code to the origin, with "git pull".  This will make sure that the version you are working on has any changes already made by a team member.
5. Now you can add your changes with git add, git commit -m "msg", and git push origin.
6. Check git log to see the changes.  
-- Now the origin should have any changes that you made.
## More git commands for collaboration:
1. **git status**: Will output changes in local & staging areas
2. **git diff**: Will output changes in local area only
3. **git diff --staged**: Will output changes in staging area only
4. **git log**: will give a history of commit, starting with most recent. Includes info such as author, date/time, commit msg, commit hash
5. **git show**: without a suffix, this will give more info on the most recent commit, including all the info in the git log + show the actual differences (aka changes)
6. **git show <unique_hash>**:  In this command, you are requesting info about a specific commit by using the hash. This gives all info listed above for the specific commit you request.  You only need to use about the first 7digits of the hash (or can use the whole thing)
7. **git reset --soft HEAD^**:  Beware! Not best practice.  This will move the most recent commit changes back to the staging area (out of the remote repo back to your local computer).  Best practice is to instead do a new commit and make changes from there, rather than try to erase the commit history.