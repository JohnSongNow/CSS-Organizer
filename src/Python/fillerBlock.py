class FillerBlock():
    """
    A single filler block in CSS-Organizer, usually reserved for comments
    and misc stuff in between regular property blocks. Note that by default
    fillerBlocks do not trim the extra new lines at the start and end
    of the block.
    """

    def __init__(self, lines):
        self._lines = lines

    def __str__(self):
        """
        Returns the block as a string
        with it's name and properties.
        """
        return "Filler block containing : " + str(self._lines)

    def add_prop(self, line):
        '''
        Adds a new line to the list of lines
        '''
        self._lines.append(line)

    def get_lines(self):
        '''
        Returns the a list of the given
        lines of the given block.
        '''
        return self._lines

    def __repr__(self):
        '''
        Returns the block as a string
        with it's name and properties.
        '''
        return str(self)

    def trim(self):
        """
        Returns the block as a string
        with it's name and properties.
        """
        list(filter(("\n").__ne__, self._lines))

    def organize(self, options, order):
        """
        Organizes filler block by trimming out leading and ending
        new lines
        """
        self.trim()