from block import *
from fillerBlock import *

class Page():
    """
    A Page class used to store multiple blocks to be used by the
    CSS-Organizer, the Page class acts as 1 CSS file as a whole and
    can be used to format the entire file.

    Attributes:
        _blocks: A list of all the CSS blocks in the page
        _length: the number of blocks in the page
    """

    def __init__(self, name, blocks):
        self._name = name
        self._blocks = blocks
        self._length = len(blocks)

    def get_blocks(self):
        '''
        Returns the blocks within the page.
        '''
        return self._blocks

    def add_block(self, block):
        '''
        Adds the blocks to to the page.
        '''
        self._blocks.append(block)
        self._length += 1

    def set_blocks(self, blocks):
        '''
        Sets the block of the following page.
        Note that both blocks and length are
        reset.
        '''
        self._blocks = blocks
        self._length = len(blocks)

    def get_name(self):
        '''
        Returns the name of the page.
        '''
        return self._name

    def __str__(self):
        """
        Returns a str representation of the page.
        """
        return 'Page(' + self._name + ')' + str(self._blocks)

    def organize(self, options, order):
        """
        Organizes the page by organizing the blocks.
        Takes in an option dict and orders them.
        """
        for block in self._blocks:
            block.organize(options, order)

    def is_valid(self):
        """
        Checks if the current page and it's
        blocks are valid.
        """

    def get_last_block(self):
        '''
        Gets the last block of the page,
        will return None if no block is present.
        '''
        if(self._length > 0):
            return self._blocks[self._length - 1]
        return None