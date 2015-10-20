from page import *
from block import *
from property import *


OPTIONS = dict()


def importCssFile():
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
