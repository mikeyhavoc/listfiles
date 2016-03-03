# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated:
# version: 0.5
import os,sys

#Folder os walk folder, subdirectory, filenames
def search_folder(folder):
    '''list directory of incoming path'''

    for filenames in os.listdir(folder):

        for file_name in filenames:
            print(file_name)

search_folder('C:\\Users\\mjwil\\documents\\github\\portfolio\\python\\listfiles')


#TODO send filenames to text file.
#list_receiver = open('output_file' + str(counter) + '.txt','w')  # text file to write output list too.  - w - creates text file if none exists.

#TODO give file path for folder to os.walk (version 2)

#TODO add yyyy-mm-dd-files.txt (version 3)

#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
