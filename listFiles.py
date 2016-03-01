# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated:
# version: 0.5
import = os,sys

#Folder os walk folder, subdirectory, filenames
def search_folder(folder):
    '''walks folder path from top node(folder) too nodes(files)'''
    for folder, subdirectory, files in os.walk(folder):

        folder = os.path.abspath(folder) # make sure it is the absolute path.
        

#TODO create text file

#TODO send filenames to text file.

#TODO give file path for folder to os.walk (version 2)

#TODO add yyyy-mm-dd-files.txt (version 3)

#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
