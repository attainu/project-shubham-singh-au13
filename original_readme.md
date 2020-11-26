# JUNK FILE ORGANISER
Basically, as a lazy programmer my desktop is full of files (Junk Files).
Due to the large number of files, it is a daunting task to sit and
organize each file. To make that task easy the below Python script
comes handy and all the files are organized in a well-manner within
seconds.
For using without any outside library installed, download this file and
use it
## Main functionality of this code
```
1.Organize by extension
2.Organize by size
3.Organize by Number of days
4.Organise ordered file into junk file
```
### How to use this::
#### First Some choices are appear like-
On basis of Choices User give some input if user give the path after
that he give choice
Than after that the on basis of that choices file is organise.
After Execution of program the file look like as shown in figure
Things that going to preform in the program -
```
1. Organise by extension
   by using this option user can organize their files by their file extension
   in a given folder, folder will be created according to file extension and
   finally all files will be moved to a created folder.
2. Organise by size
   by using this option user can organize their files by their file size,
   according to file sizes random folders will be created and respective
   files will be moved to them.
3. Organise by Last used/accessed date
   by using this option user can organize their files by last used date.
   random folders will be created according to files last used date and
   files will be moved to them.
4. Convert well organised file into junk file
   By using this option our organised file is converted into junk file and all
   the extra folder are get deleted.
```
#### What i used :
I used many built-in libraries like- shutil for file movement,datetime for
get the date of the files,argparse for the command line parsing and
etc.
#### Future improvement:
We can design the ui for the program so a normal user can easily
interact with it. We can add more features like deleting the junk files
after a certain period of time.
### Note
If a user want zunk file instead of well organised file than the
program will gone to perform that task and if user organise a file with
different type by mistake than he run the program and organise that in
there choice
### Note
if user not provide any think or user provide wrong path than
program will tell to provide vaild thing.