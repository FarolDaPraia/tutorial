https://www.youtube.com/watch?v=HVsySz-h9r4

# Command Line  
## working directory  
* git version  
$ git -- version  
* Set Config Values  
$ git config --global user.name "Alexandre Tsuno"  
$ git config --global user.email "aletsuno@goolemail.com"  
* check the values with  
$ git config --list  
* need help  
$ git help <verb\>  

## initialize repository  
* initialize a repository from existing code local code base that you want to
start tracking using git  
$ git init  
$ git status  
* create a ignore file:  
 * in git bash  
$ touch .gitignore  
 * in windows  
Create the text file gitignore.txt  
Then rename the file in the command line, with ren gitignore.txt .gitignore  
 * in .gitignore file add all file and directory that git shall gitignore  
* [where are you]  

* clone  
$ git clone <url/where to clone\>  
* pushing changes previously  

* create a branch for desired feature  
$ git branch <feature name\>  
$ git checkout <feature name\>  
to work on the branch  

![where are you](./46_GIT/where_are_now.JPG)  

## git remote  
* viewing information about the remote repository  
$ git remote  
list the remote connections you have to other repositories  
$ git remote -v  
list but include the URL of each connection  
* Create a new connection to a remote repository  
$ git remote add <name\> <url\>  
* Remove the connection to the remote repository called  
$ git remote rm <name\>  
* Rename a remote connection from to  
$ git remote rename <old-name\> <new-name\>  
* Set URL
$ git remote set-url <https: repository>

## git fetch  
The git fetch command downloads commits, files, and refs from a remote
repository into your local repo. Fetching is what you do when you want to
see what everybody else has been working on, but it doesn’t force you to
actually merge the changes into your repository.  
Git keeps remote and local branch commits distinctly separate through the
use of branch refs. The refs for local branches are stored in the ./.git/
refs/heads/. Remote branch refs live in the ./.git/refs/remotes/  
* a  list of the local branch refs  
$ git branch -a  
* remote branch are prefixed by the remote they belong  
$ git branch -r  
* downloads all of the required commits and files from the other repository  
$ git fetch <remote\> <branch\>  
* all registered remotes and their branches  
$ git fetch --all  
* perform a demo run of the command  
It will output examples of actions it will take during the fetch but not
apply them.  
$ git fetch --dry-run  
* synch origin with git fetch  
synchronizing your local repository with the central repository's master
branch  
$ git fetch origin  
 * to see what commits have been added to the upstream master  
 $ git log --oneline master..origin/master  
 * to approve the changes and merge them into your local master branch  
 $ git checkout master
 $ git merge origin/master

## git branch
* to create a branch
$ git branch <branch_name>
$ git checkout <branch_name>
* to delete a branch after merge
$ git branch -d <branch_name>  
* to delete a branch bevor merge
$ git branch -D <branch_name>

* to create a branch and checkout
$ git checkout -b <branch_name>

## git merge
* workflow
$ git checkout master
$ git merge <feature_name>

## git push  
* upload local repository content to a remote repository  
$ git push <remote\> <branch\>    
* example:
$ git checkout master  
$ git fetch origin master  
$ git rebase -i origin/master  \#Squash commits, fix up commit messages etc.  
$ git push origin master  
* deleting a branch  
$ git branch --merged  
$ git branch -d <feature name\>  //e.g git branch -d fix/authentication  
$ git branch -a  
$ git push <repository name\> --delete <feature name\>  //git push origin --delete fix/
authentication   
or  
$ git branch -D branch_name  
$ git push origin :branch_name //git push origin :fix/authentication  

* If you get the error below, it may mean that someone else has already deleted the branch.  
The -p flag means "prune". After fetching, branches which no longer exist on the remote will be
deleted.  
$ git fetch -p


## staging area  
* add file to staging area  
$ git add <file name\>  
or  
$ git add -A  
to add all file in the directory  
* to remove file from staging area  
$ git reset HEAD <file name\>  
or  
$ git reset  
remove all <file name\>  
or  
$ git rm <file name\>  
* undo a working change
$ git checkout -- <file name\>


* first commit  
$ git commit -m "message commit"  
* log  
$ git log  
* log change from each commit
$ git log -p
* difference made in code to working directory  
$ git diff  
* diff from staging area to history
$ git diff --staged

## Connecting to GitHub with SSH  
### checking for existing SSH keys  
* open Git Bash  
* Enter ls -al ~/.ssh  

### generating a new SSH key  
* open Git Bash  
* Enter $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"  

### adding ssh key to the ssh-agent  
* $ eval $(ssh-agent -s)  
\> Agent pid 59566  
* $ ssh-add ~/.ssh/id_rsa  
* Copy the SSH key to your clipboard  
$ clip < ~/.ssh/id_rsa.pub  
* testing connection  
$ ssh -T git@github.com  

## git rename remove file  
* rename file  
$ git mv <old_filename> <new_filename>  
* move to another folder and rename file  
$ git mv <old_filename> <folder_name>/<new_filename>  
* remove file only from remote  
$ git rm --cached <filename>  
* remove folder and all file only from remote  
$ git rm --cached -r <folder_name>
