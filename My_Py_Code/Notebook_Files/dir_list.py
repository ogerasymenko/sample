'''
Function for display files in current directory and sub directories.
'''

__author__ = 'sashko'

# will be use os module
import os


# define function
def list_dir(dirname='.'):
    ''' os.walk return 3 tuples, by 'for' cycle for each item will be join
    path of file to current dir by os.path.join method '''
    for (currDir, subdirNames, fileNames) in os.walk(dirname):
            # use sorted() function to sort output
            for fileName in fileNames:
                if fileName.startswith("Unt"):
                    print(fileName)

# call function
list_dir('.')
