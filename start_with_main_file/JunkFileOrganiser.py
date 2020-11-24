from PathOrganise import PATHORGANISERS
from Timeandate import DATESANDTIMES
from SizeModification import SIZEORGANISER

class JunkFileOrganiser:
    def __init__(self):
        self.DIRECTORY_PATH='C:\\Users\\Mau\\Desktop\\testing'+'\\'
        self.SOURCE_PATH=r'C:\Users\Mau\Desktop\testing'+'\\'
    def extension(self,x):
        PATHORGANISERS(x)

    def DATES(self,x):
        DATESANDTIMES(x)

    def SIZE(self,x):
        SIZEORGANISER(x)
def Dictionary(X,Y):
    d={1:"ORGANISE BY Extension\n",2:"ORGANISE BY DATE\n",3:"ORGANISE BY SIZE\n"}
    if len(X)==1 or len(X)==0:
        return
    inputTakerr(X,Y)
    print(d[Y])


def inputTakerr(X,Y):
    obj=JunkFileOrganiser()
    if Y == 1:
        obj.extension(X)
    if Y == 2:
        obj.DATES(X)
    if Y == 3:
        obj.SIZE(X)
    if Y > 3:
        print("Invalid Choice")


if __name__ == "__main__":
   X = input("Enter The Path\n")
   X=r''+X+'\\'
   d={1:print("1.ORGANISE BY Extension\n"),2:print("2.ORGANISE BY DATE\n"),3:print("3.ORGANISE BY SIZE\n")}
   Y =int(input("ENTER THE CHOICE\n"))
   Dictionary(X,Y)
