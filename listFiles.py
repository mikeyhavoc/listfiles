# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated:
# version: 1.0
import os,sys

#Folder os walk folder, subdirectory, filenames
def search_folder(folder):
    '''list directory of incoming path'''
    for filenames in os.listdir(folder):

     return filenames

#Send filenames to text file.
def file_to_text(file_names):
    text_file_name = input('please name text file ')
    print('creating text file...')
    # text file to write output list too.  - w - creates text file
    list_receiver = open(text_file_name  + '.txt','w')
    file.write(list_receiver, file_names)
    list_receiver.close()







path = os.getcwd()
file_names = search_folder(path)
file_to_text(file_names)
#TODO give file path for folder to os.walk (version 2)

#TODO add yyyy-mm-dd-files.txt (version 3)

#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
