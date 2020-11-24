from Checker import main
from JunkFileOrganiser import Dictionary
class Execution:
    def __init__(self,path,y):
        self.DIRECTORY_PATH=path
        self.SOURCE_PATH=path
        self.Y=y
        if y == 4:
            print("Enter the Valid Choice")
            return
        main(self.SOURCE_PATH,self.DIRECTORY_PATH)
    def Run(self):
        if self.Y == 4:
            return
        Dictionary(self.DIRECTORY_PATH,self.Y)
    
    


if __name__ == "__main__":
    X=input("ENTER THE PATH\n")
    X=r''+X+'\\'
    d={1:print("1.ORGANISE BY Extension\n"),2:print("2.ORGANISE BY DATE\n"),3:print("3.ORGANISE BY SIZE\n")}
    Y=int(input("Enter The Choice\n"))
    obj=Execution(X,Y)
    obj.Run()


    
