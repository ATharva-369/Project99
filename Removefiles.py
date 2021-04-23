'''
This program deletes files and folders older than 30 days. It uses an input for the directory and it cleans the directory's subfolders and files.
It uses the os.stat().st_ctime property to get the time the file or folder was created.
'''
#importing the modules required
import shutil
import os
import time
#using text input for the path
path = input("enter the directory to be cleaned: ")
#creating a days variable to store the current time
days = time.time()
#checking if the path exists
if os.path.exists(path):
    #storing all the subfolders and files into the 'files' variable
    files = os.listdir(path)
    for i in files:
        i = os.path.join(path, i)
        name,ext = os.path.splitext(i)
        ext = ext[1:]
        #checking if  path+i is a folder or file
        if ext == '':
            if os.stat(i).st_ctime <= -30*24*60+time.time():
                shutil.rmtree(i)
                print("folders older than 30 days have been deleted")
                print("------------------------------------------")
            else:
                print("folders: everything is already clean :) ")
                print("------------------------------------------")
        else:
            if os.stat(i).st_ctime <= -30*24*60+time.time():
                os.remove(i)
                print("files older than 30 days have been deleted")
                print("------------------------------------------")
            else:
                print("files: everything is already clean :) ")
                print("------------------------------------------")
else:
    print("this directory does not exist")
