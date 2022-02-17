import os
import shutil

# Get path from the user
path = input("Enter the Path: ")
files = os.listdir(path)
for file in files:
    # Split the filename and extension
    filename,extension = os.path.splitext(file)
    # Remove the . from final extension
    extension = extension[1:]
    if os.path.exists(path+ '/' + extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.mkdir(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
