import os


def list_dir(dirname='.'):
    ''' os.walk return 3 tuples, by 'for' cycle for each item will be join
    path of file to current dir by os.path.join method '''
    for (currDir, subdirNames, fileNames) in os.walk(dirname):
        for fileName in fileNames:
            if fileName.startswith('sess_'):
                os.remove(fileName)

# call function
list_dir()
