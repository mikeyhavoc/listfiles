# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated: 3/6/16
# version: 2.5
import os,sys,datetime

#Folder os walk folder, subdirectory, filenames
def list_files_in_text(folder):
    '''list directory of incoming path
       opens list_receiver name text
       file being created. for file in
       dirs print files. close list_receiver
    '''

    path = folder
    files = os.listdir( path )

    text_file_name = input('please name text file ')
    print('creating text file...')
    # text file to write output list too.  - w - creates text file
    list_receiver = open(text_file_name  + '.txt','w')

    for file_names in files:
        if file_names.startswith('.'):
            continue
        files = list_receiver.write(file_names)
        line_space = list_receiver.write('\n')

    list_receiver.close() # close txt file.

#File path for folder to listdir version 2.5
def file_path():
    '''directory left empty takes path listfiles.py is
       currently in, or can enter desired path for
       directory
    '''
    directory_name = input('please give directory path ')
    if directory_name == '' or directory_name == None:
        return os.getcwd()
    elif directory_name != None:
        return directory_name

path = os.getcwd()
directory_name = file_path()
list_files_in_text(directory_name)


#TODO add yyyy-mm-dd-files.txt (version 3)

#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
