# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated: 3/11/16
# version: 3
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
        if file_names.startswith('.'):          # all directories excluded
            continue
        files = list_receiver.write(file_names)
        line_space = list_receiver.write('\n')

    list_receiver.close() # close txt file.
    return text_file_name
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

#Timestamp yyyy-mm-dd-files.txt (version 3.5)
def time_stamp(text_file_name):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    date_file_name = str(year) + '-' + str(month) + '-' + str(day) + '_' +  str(text_file_name) + '.txt'
    #text_name = text_file_name + '.txt'
    date_name = input('update name to yyyy-mm-dd-filename? ')
    if date_name == 'yes' or date_name == 'y':
        return os.rename(text_file_name , date_file_name)
    elif date_name == 'no' or date_name == 'n':
        return text_file_name


#path = os.getcwd()
directory_name = file_path()
name = list_files_in_text(directory_name)
time_stamp(name)







#TODO be able to alter filename - yyyy-mm-dd-filename.txt (version 4)
