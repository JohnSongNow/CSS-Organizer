from property import *
from block import *
from page import *

import traceback


FILE_LIMIT = 25
FILE_SIZE_LIMIT = 5000

def organize_files(file_names, file_path):
    '''
    ([Str], Str) -> NoneType
    Imports CSS files and exports an organized
    verison of those pages.
    '''
    options = dict()
    pages = []

    # Importing the options
    options = load_options(file_path)

    # Importing the CSS Pages
    pages = import_CSS_files(file_names, file_path)

    print(pages[1])
    # Exporting the CSS Pages
    # export_CSS_files(file_path, pages)


def import_CSS_files(file_names, file_path='', reset=True):
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
        except FileNotFoundError:
            print(file_name + ' was not found')
    return PAGES


def export_CSS_files(dir_name, pages):
    '''
    ([Str], Str) -> NoneType
    Transforms the current Page Objects into
    CSS files and exports them to a dir
    '''
    for page in pages:
        try:
            # Writing the file
            with open('export-test' + '.css', 'w') as f:
                for block in page.get_blocks():
                    print(block)
                    for prop in block.get_props():
                        print(prop)
                f.close()
        except FileNotFoundError:
            print('Error exporting ' + page.get_name() + '.css')


def lines_to_page(name, lines):
    '''
    Returns a page object of the following
    line-parsed CSS file, note that if the
    lines are not valid an expection will be
    thrown.
    '''
    # Making the starting variables for the loop
    new_page = Page(name, [])
    in_block = False

    # Looping through the CSS lines
    for line in lines:
        # Replacing tabs
        line = line.lstrip()


        # Checking if we've started or ended a new block
        if('{' in line or '}' in line):
            in_block = not in_block
            # If we have a new block add it
            if(in_block):
                line = line.replace('{', '')
                new_page.add_block(Block(line, []))
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

    return new_page


def page_to_lines(file_name, dir_location):
    '''
    (Str) -> NoneType
    Changes the page object back into a file and write it
    into the directory
    '''
    pass


def add_CSS_File(file_names, file_path=''):
    '''
    (Str, Str) -> NoneType
    Adds a CSS file into the existing PAGES list.
    Calls importCSSPages while not reseting our
    current pages.
    '''
    import_CSS_files(file_name, file_path, False)


def load_options(file_path):
    """
    Loads the options from the text file into
    the options DICT. Note that if no options file
    is found a text file will be created in the dir
    of this file.
    """
    # Resetting out previous options
    options = dict()
    current_lines = []
    try:
        # Reading files
        with open(file_path + 'options.txt') as f:
            current_lines = f.read().splitlines()
            # Changing to pages
            f.close()
    except:
        print('options.txt' + ' does not exist')

    for line in current_lines:
        lines = line.split(':')
        OPTIONS[lines[0]] = lines[1]
    return options

organize_files(['expected-test', 'initial-test'], 'test/')