from block import *


class Page():
    """
    A Page class used to store multiple blocks to be used by the
    CSS-Organizer, the Page class acts as 1 CSS file as a whole and
    can be used to format the entire file.

    Attributes:
        _blocks: A list of all the CSS blocks in the page
        _length: the number of blocks in the page
    """

    def __init__(self, blocks=[]):
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


    def set_blocks(self, block):
        '''
        Sets the block of the folowing keyboards
        '''

    def __str__(self):
        """
        """
        return str(self._blocks)

    def organize(self):
        """
        """

    def is_Valid(self):
        """
        """

    def get_last_block(self):
        '''
        Gets the last block of the page,
        will return None if no block is present.
        '''
        if(self._length > 0):
            return self._blocks[self._length - 1]
        return None