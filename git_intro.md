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