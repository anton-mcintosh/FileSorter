import os
import shutil
from datetime import datetime

downloads = '/Users/anthonymcintosh/downloads'
screenshots = '/Users/anthonymcintosh/desktop/screenshots'

# Sorts the files in the downloads folder into folders based on their file extension
def sortDownloads():
    list_ = os.listdir(downloads)
    for file_ in list_:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
        if ext == '':
            continue
        if os.path.exists(downloads+'/'+ext):
            shutil.move(downloads+'/'+file_, downloads+'/'+ext+'/'+file_)
        else:
            os.makedirs(downloads+'/'+ext)
            shutil.move(downloads+'/'+file_, downloads+'/'+ext+'/'+file_)

# Sorts the files in the screenshots folder into folders based on their creation date
def sortScreenshots():
    list_ = os.listdir(screenshots)
    sorted_list = sorted(list_, key=lambda x: os.path.getctime(os.path.join(screenshots, x)))
    for file_ in sorted_list:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
        if ext == '':
            continue

        #Get the creation time of the file
        creation_time = os.path.getctime(os.path.join(screenshots, file_))
        creation_date = datetime.fromtimestamp(creation_time).date()

        #Create the destination folder based on the creation date
        dest_folder = os.path.join(screenshots, str(creation_date))


        #Move the file to the destination folder
        if os.path.exists(dest_folder):
            shutil.move(os.path.join(screenshots, file_), os.path.join(dest_folder, file_))
        else:
            os.makedirs(dest_folder)
            shutil.move(os.path.join(screenshots, file_), os.path.join(dest_folder, file_))

sortDownloads()
sortScreenshots()