# Used for python executable
#!/usr/bin/python
import json

from property import *
from block import *
from page import *

FILE_LIMIT = 25
FILE_SIZE_LIMIT = 5000

def organize_files(file_names):
    '''
    ([Str], Str) -> NoneType
    Imports CSS files and exports an organized
    verison of those pages.
    '''
    options = dict()
    pages = []

    # Importing the options
    options = load_options()

    # Importing the CSS Pages
    pages = import_CSS_files(file_names)

    # Organizes the CSS pages
    pages = organize_pages(pages, options)

    # Exporting the CSS Pages
    export_CSS_files(pages)


def import_CSS_files(file_names, reset=True):
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
            with open(file_name + '.css') as f:
                current_lines = f.read().splitlines()
                # Changing to pages
                PAGES.append(lines_to_page(file_name, current_lines))
                f.close()
        except FileNotFoundError:
            print(file_name + ' was not found')
    return PAGES


def export_CSS_files(pages, dir_name=''):
    '''
    ([Str], Str) -> NoneType
    Transforms the current Page Objects into
    CSS files and exports them to a dir
    '''
    # Used for indenting
    tab_num = 0
    tabs = ''

    for key, value in pages.items():
        try:
            # Writing the file
            with open(dir_name + key + '-finale' + '.css', 'w') as f:
                # Writing out the line
                for line in value:
                    f.write(line)
                f.close()
        except FileNotFoundError:
            print('Error exporting ' + key + '.css')


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
    in_comment = False

    # Looping through the CSS lines
    for line in lines:
        # Replacing tabs
        line = line.lstrip()
        line = line.rstrip()

        # Empty line
        if(line == ''):
            pass
        else:
            else:
                # Else if we are not in a comment block and non empy line
                # Checking if we've started or ended a new block
                if('{' == line[0] or '}' == line[0]):
                    in_block = not in_block
                    # If we have a new block add it
                    if(in_block):
                        line = line.replace('{', '')
                        line = line.rstrip()
                        new_page.add_block(Block(line, []))
                    else:
                        in_block = False
                # If we're closing a block
                else:
                    # Splitting and adding the prop
                    line = line.replace(';', '')
                    prop_list = line.split(':')
                    new_prop = Property(prop_list[0], prop_list[1].lstrip())
                    new_page.get_last_block().add_prop(new_prop)
    return new_page


def page_to_lines(pages, options):
    '''
    ([Page]) -> dict(Str : [Str])
    Changes the page object back into a file and write it
    into the directory
    '''
    # Dict for lines
    lines = dict()

    for page in pages:
        # Temp storage for the lines
        temp_page = []
        # Setting the name
        lines[page.get_name()] = temp_page

        # Writing each block
        for block in page.get_blocks():
            # Writing each name in the block
            for name in block.get_names():

                temp_page.append(name)
                temp_page.append(' ')
            temp_page.append("{\n")

            # Writing each prop
            for prop in block.get_props():
                temp_page.append('\t' + prop.get_value() +  '\n')

            temp_page.append("} \n")
            temp_page.append("\n")
    return lines


def load_options():
    """
    (Str) -> {Dict}
    Loads the options from the text file into
    the options DICT. Note that if no options file
    is found a text file will be created in the dir
    of this file.
    """
    options = dict()
    # Resetting out previous options
    try:
        f = open('options.txt', 'r')
        options_str = ''
        for line in f:
            options_str += line

        options = json.loads(options_str)
    except ValueError:
        print('Loading Options Failed')

    return options


def organize_pages(pages, options):
    '''
    ([Pages], {Str : Obj}) -> Pages
    Organizes each of the indiviudal pages based
    on the options given.
    '''
    # Organizes each page
    for page in pages:
        page.organize(options)
    # Transforming the pages into lines
    pages = page_to_lines(pages, options)
    return pages


organize_files(['../test/expected-test', '../test/initial-test',
                '../test/multitag-test', '../test/danny-test'])

'''
# If we have invalid argurments
if len(sys.argv) > 10 or len(sys.argv) < 2:
    print('Invalid Arguments')
else:
    # Parse the argument
    print(sys.argv[0])
    print(sys.argv[1])

    file_names = []
    # If the second args wants the whole page
    if(sys.argv[1].lower() == 'a'):
        file_names = glob.glob(os.getcwd() + '/*.css')

    print(os.getcwd() + '/*.css')
    print(file_names)
    # Calling file organization
    organize_files(file_names, os.getcwd())
'''