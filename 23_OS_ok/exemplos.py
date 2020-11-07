import os

#get current directory
print(os.getcwd())
#C:\Users\alexa\Documents\BitsBytes\tutorial\23_OS

#change directory. Use /
os.chdir('C:/Users/alexa/Documents/BitsBytes/')
print(os.getcwd())

#return list of folders and files in directory
print(os.listdir())

#create folders
#os.mkdir(path) -> one directory
#os.makedirs(path) -> create directory and sub-directorys
#       -> best Use

#deleate folders
#os.rmdir(path) -> best use
#os.removedirs(path)

#rename file
#os.rename(old,new)

#read some information about file
from datetime import datetime
mod_time = os.stat('kite_tutorial.py').st_mtime
print(datetime.fromtimestamp(mod_time))
#.st_size file size
#.st_mtime last modification time

#yields the directory path, the directory within that path and the files within that path
#os.walk(path)
for dirpath, dirnames, filenames in os.walk('C:/Users/alexa/Documents/BitsBytes/book'):
    print('current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)

#get environment variables
#os.environ.get(key)

#os.path.join(path, filename)
