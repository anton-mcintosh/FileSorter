import os
import shutil
from datetime import datetime



## sortDownloads
# Sorts the files in the downloads folder into folders based on their file extension
# If the folder does not exist, it will be created.
##
def sortByType():
    list_ = os.listdir(path)
    for file_ in list_:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
        if ext == '':
            continue
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

## sortScreenshots
#  Sorts the files in the screenshots folder into folders based on their creation date.
# If the folder does not exist, it will be created.
##
def sortByDate():
    list_ = os.listdir(path)
    sorted_list = sorted(list_, key=lambda x: os.path.getctime(os.path.join(path, x)))
    for file_ in sorted_list:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
        if ext == '':
            continue

        #Get the creation time of the file
        creation_time = os.path.getctime(os.path.join(path, file_))
        creation_date = datetime.fromtimestamp(creation_time).date()

        #Create the destination folder based on the creation date
        dest_folder = os.path.join(path, str(creation_date))


        #Move the file to the destination folder
        if os.path.exists(dest_folder):
            shutil.move(os.path.join(path, file_), os.path.join(dest_folder, file_))
        else:
            os.makedirs(dest_folder)
            shutil.move(os.path.join(path, file_), os.path.join(dest_folder, file_))

print("What file path would you like to sort?")
path = input()
print("How would you like to sort those files?")
print("Enter 1 to sort by file type, and 2 to sort by date")
sort_type = input()

if sort_type == "1":
    sortByType()
else:
    sortByDate()