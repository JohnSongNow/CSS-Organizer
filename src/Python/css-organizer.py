from property import *
from block import *
from page import *
import traceback

OPTIONS = dict()

FILE_LIMIT = 25
FILE_SIZE_LIMIT = 5000
PAGES = []

def importCSSPAGES(file_names, file_path='', reset=True):
    '''
    ([Str], Str) -> NoneType
    Imports the CSS PAGES in a directory into
    the PAGES list, note that the PAGES are
    cleared before imported.
    '''
    PAGES = []

    # Reading and converting each file into a Page Object
    for file_name in file_names:
        try:
            # Reading files
            with open(file_path + file_name + '.css') as f:
                current_lines = f.read().splitlines()
                # Changing to pages
                PAGES.append(lines_to_page(file_name, current_lines))
                f.close()
        except:
            print(file_name + ' does not exist')
    print(PAGES[0])
    return


def lines_to_page(name, lines):
    '''
    Returns a page object of the following
    line-parsed CSS file, note that if the
    lines are not valid an expection will be
    thrown.
    '''
    # Making the starting variables for the loop
    new_page = Page(name)
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


def page_to_file(dir_location):
    '''
    (Str) -> NoneType
    Changes the page object back into a file and write it
    into the directory
    '''
    pass


def addCSSFile(file_names, file_path=''):
    '''
    (Str, Str) -> NoneType
    Adds a CSS file into the existing PAGES list.
    Calls importCSSPages while not reseting our
    current pages.
    '''
    importCSSPAGES(file_name, file_path, False)


def loadOptions():
    """
    Loads the options from the text file into
    the options DICT. Note that if no options file
    is found a text file will be created in the dir
    of this file.
    """
    return

# Printing out the block
importCSSPAGES(['expected-test', 'initial-test'], 'test/')