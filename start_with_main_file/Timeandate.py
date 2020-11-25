import os
import datetime
from pathlib import Path

class Timeandate:
    def folderCreation(self,date_folder,DIRECTORY_PATH):
        for dates in date_folder:
            if dates==0:
                FOLDER_NAME = "File created From day-0 to day-9"
            elif dates == 10:
                FOLDER_NAME = "File created From day-10 to day-19"
            elif dates == 20:
                FOLDER_NAME = "File created From day-20 to day-29"
            elif dates==30:
                FOLDER_NAME = "File created From day-30 to day-39"
            elif dates == 40:
                FOLDER_NAME= "File created From day-40 to day-59"
            elif dates == 60:
                FOLDER_NAME = "File created From day-60 to day-89"
            else:
                FOLDER_NAME= "File created From day-90 and onwards"
            directories_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME)  
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)


    def onlyfile(self,files,DIRECTORY_PATH,only_files):
        for current_file in files:
            old_path = os.path.join(DIRECTORY_PATH,current_file)
            isFile = os.path.isdir(old_path) #Checking the current file is file or directory if directory than dont include
            if isFile == True:
                continue
            only_files.append(current_file)


    def totaldays(self,only_files,DIRECTORY_PATH,mover):
        for file in only_files:
            mtime = (os.stat(os.path.join(DIRECTORY_PATH, file)).st_mtime)               # give the time from 1991
            timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')      #give  year month and day on which day file is created
            cur_date = datetime.datetime.now().strftime('%Y-%m-%d')                       #Give todat date and time
            d1 = datetime.date(int(timestamp[:4]), int(timestamp[5:7]), int(timestamp[8:]))#stored on which day file is created
            d2 = datetime.date(int(cur_date[:4]), int(cur_date[5:7]), int(cur_date[8:]))    #current date is stored
            d3=(d2-d1).days                                                                 #print the number of days from file creted till today
            old_path = os.path.join(DIRECTORY_PATH,file)                                    #Current Directory Path
            mover.append([d3,old_path,file])
    def moves(self,mover,DIRECTORY_PATH):
        for days,old_path,file in mover:
            isFile = os.path.isdir(old_path)       # checking if it is a file or directory if it is directory than ignore it  
            if(isFile)==True:
                continue
            if days>=0 and days<=9:
                FOLDER_NAME = "File created From day-0 to day-9"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            elif days >= 10 and days<=19:
                FOLDER_NAME = "File created From day-10 to day-19"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            elif days >= 20 and days <= 29:
                FOLDER_NAME = "File created From day-20 to day-29"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            elif days >= 30 and days <= 39:
                FOLDER_NAME= "File created From day-30 to day-39"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            elif days >= 40 and days <= 59:
                FOLDER_NAME= "File created From day-40 to day-59"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            elif days >= 60 and days <= 89: 
                FOLDER_NAME= "File created From day-60 to day-89"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
            else:
                FOLDER_NAME= "File created From day-90 and onwards"
                new_path = os.path.join(DIRECTORY_PATH,FOLDER_NAME,file)
                os.rename(old_path, new_path)
    def extrafolder(self,DIRECTORY_PATH):
        folders = list(os.walk(DIRECTORY_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])

def DATESANDTIMES(DIRECTORY_PATH):
    files = os.listdir(DIRECTORY_PATH)
    only_files = []
    date_folder = [0,10,20,30,40,60,90] 
    mover = []
    obj = Timeandate()
    obj.folderCreation(date_folder,DIRECTORY_PATH)
    obj.onlyfile(files,DIRECTORY_PATH,only_files)
    obj.totaldays(only_files,DIRECTORY_PATH,mover)
    obj.moves(mover,DIRECTORY_PATH)
    obj.extrafolder(DIRECTORY_PATH)





