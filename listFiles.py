# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated:
# version: 1.0
import os,sys

#Folder os walk folder, subdirectory, filenames
def list_files_in_text(folder):
    '''list directory of incoming path
       opens list_receiver name text
       file being created. for file in
       dirs print files. close list_receiver
    '''

    path = folder
    dirs = os.listdir( path )

    text_file_name = input('please name text file ')
    print('creating text file...')
    # text file to write output list too.  - w - creates text file
    list_receiver = open(text_file_name  + '.txt','w')

    # print all files and directories
    for file_names in dirs:
         files = list_receiver.write(file_names) # write files to txt file.
         line_space = list_receiver.write('\n')

    list_receiver.close() # close txt file.


path = os.getcwd()
list_files_in_text(path)

#TODO give file path for folder to os.walk (version 2)

#TODO add yyyy-mm-dd-files.txt (version 3)

#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
