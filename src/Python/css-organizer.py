from property import *
from block import *
from page import *

OPTIONS = dict()

FILE_LIMIT = 25
FILE_SIZE_LIMIT = 5000
FILES = []

def importCSSFiles(file_names, file_path=''):
    '''
    Imports the CSS files in a directory into
    the files list, note that the files are
    cleared before imported.
    '''
    FILES = []

    # Reading and storing the lines in our array
    for file_name in file_names:
        with open(file_path + file_name + '.css') as f:
            FILES.append(f.read().splitlines())
            f.close()

    print(FILES[0])
    return

def text_to_page(lines):
    '''
    Returns the
    '''
    return

def addCSSFile(file_names, file_part=''):
    '''
    Adds a CSS file into the existing files list.
    '''
    return


def loadOptions():
    """
    Loads the options from the text file into
    the options DICT. Note that if no options file
    is found a text file will be created in the dir
    of this file.
    """
    return


test_block = Block("Test Block")
test_prop = Property("Test", 10)
test_prop2 = Property("Test", 25)

test_block.addProp(test_prop)
test_block.addProp(test_prop2)

# Printing out the block
print(test_block)

importCSSFiles(['expected-test', 'initial-test'], 'test/')