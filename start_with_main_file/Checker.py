import os
# x=input() #PATH OF FILE LOCATION

class Checker:
    def filechecker(self,SOURCE_PATH,DIRECTORY_PATH):
        for path,_,files in os.walk(SOURCE_PATH):
            if files:
                for Files in files:
                    if not os.path.isfile(DIRECTORY_PATH+Files):   
                        os.rename(path+'\\'+Files,DIRECTORY_PATH+Files)

    def folderremove(self,DIRECTORY_PATH):
        folders = list(os.walk(DIRECTORY_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])
def main(SOURCE_PATH,DIRECTORY_PATH):
    if len(SOURCE_PATH)==1:
        print("Enter the valid Input")
        return
    obj=Checker()
    obj.filechecker(SOURCE_PATH,DIRECTORY_PATH)
    obj.folderremove(DIRECTORY_PATH)

if __name__ == "__main__":
    DIRECTORY_PATH=''
    SOURCE_PATH=''
    main(DIRECTORY_PATH, SOURCE_PATH)

