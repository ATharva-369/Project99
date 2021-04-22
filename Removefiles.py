import shutil,os,time
path = input("enter the directory to be cleaned: ")
days = time.time()
print(days)
if os.path.exists(path):
    files=os.listdir(path)
    for i in files:
        i = os.path.join(path, i)
        name, ext=os.path.splitext(i)
        ext = ext[1:]
        if ext == '':
            if os.stat(i).st_ctime <= -30*24*60+time.time():
                shutil.rmtree(i)
        else:
            if os.stat(i).st_ctime <= -30*24*60+time.time():         
                 os.remove(i)
