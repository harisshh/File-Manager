import os
import shutil

#print(os.getcwd())

path = input("Enter the Path: ")
files = os.listdir(path)
for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+ '/' + extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.mkdir(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        