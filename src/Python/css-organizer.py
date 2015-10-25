from property import *
from block import *
from page import *
import traceback

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
        try:
            with open(file_path + file_name + '.css') as f:
                FILES.append(f.read().splitlines())
                f.close()
        except:
            print(file_name + ' does not exist')

    print(FILES[0])
    # Changing to pages
    for x in range(len(FILES)):
        FILES[x] = lines_to_page(FILES[x])
    print(FILES[0])
    return


def lines_to_page(lines):
    '''
    Returns a page object of the following
    line-parsed CSS file, note that if the
    lines are not valid an expection will be
    thrown.
    '''
    # Making the starting variables for the loop
    new_page = Page()
    in_block = False

    try:
        # Looping through the CSS lines
        for line in lines:
            # Replacing tabs
            line = line.lstrip()

            # Checking if we've started a new block
            if('{' in line or '}' in line):
                in_block = not in_block
                # If we have a new block add it
                if(in_block):
                    line = line.replace('{', '')
                    temp_block = Block(line)
                    new_page.add_block(temp_block)
                else:
                    in_block = False
            # Empty line
            elif(line == ''):
                pass
            # If we're closing a block
            else:
                # Splitting and adding the prop
                line = line.replace(';', '')
                prop_list = line.split(':')
                new_prop = Property(prop_list[0], prop_list[1].lstrip())
                new_page.get_last_block().add_prop(new_prop)
    except:
        print("Error parsing the file")
        # traceback.print_stack()
    return new_page


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

# Printing out the block
importCSSFiles(['expected-test', 'initial-test'], 'test/')