# listFiles
# author: Michael Williams
# date: 2/29/16
# description: looks through a folder and lists all files contained in said
#              folder and creates and lists them in a text document.
# updated: 3/13/16
# version: 4
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
    directory_name = input('please give directory path or use files ')
    if directory_name == '' or directory_name == None:
        return os.getcwd()
    elif directory_name != None:
        return directory_name

#Timestamp yyyy-mm-dd-files.txt (version 3.5)
def time_stamp(text_file_name):
    '''
       optionally asks if you would like to os.rename
       text_file_name to yyyy-mm-dd_filename.txt from
       filename.txt
    '''
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    date_file_name = str(year) + '-' + str(month) + '-' + str(day) + '_' +  str(text_file_name) + '.txt' # yyyy-mm-dd-filename

    text_file = text_file_name + '.txt'  # extension added for os.rename.

    date_name = input('update name to yyyy-mm-dd-filename? ')
    if date_name == 'yes' or date_name == 'y':
        return os.rename(text_file , date_file_name)
    elif date_name == 'no' or date_name == 'n':
        return text_file_name

def working_path( folder ):
    '''
       returns if yes current working directory
       if no returns listdir to working_path
    '''
    get_path = input('would you like to see the path? ')
    if get_path == 'yes' or get_path == 'y':
        print(os.getcwd())
    elif get_path == 'no' or get_path == 'n':
        return os.listdir()

#path = os.getcwd()
directory_name = file_path()
given_dir = working_path( directory_name )
name = list_files_in_text(directory_name)
time_stamp(name)
