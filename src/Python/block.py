class Block():
    """
    A single CSS Block in CSS-Organizer, contains the name and type of block
    that it is as well as contains a list of all CSS properties in the block.
    By default the block does not check if the props within the CSS is valid
    and must be explicatly called.
    """

    def __init__(self, name, props):
        self._name = name
        self._props = props

    def set_props(self, props):
        self._props = props

    def set_name(self, name):
        self._name = name

    def remove_prop_by_name(self, name):
        '''
        Removes the property within the list
        '''
        # Gets ths removed propr, None if not present
        removed_prop = self.contains_prop(name)

        # Removing the prop
        if(removed_prop == None):
            return
        self._props.remove(removed_prop)

    def get_props(self):
        '''
        Returns the a list of the given
        properties of the given block.
        '''
        return self._props

    def get_prop(self, name):
        '''
        Returns the prop with the current name,
        returns None if no prop is found.
        '''
        return None

    def contains_prop(self, name):
        """
        Checks if the block contains the property with
        the following name. If it does return the property
        """
        # New list of only the property with the wanted name
        new_list = [x for x in self._props if x.get_name() == name]

        # If nothing fits the description
        if(len(new_list) == 0):
            return None
        # Returns the first element
        return new_list[0]

    def add_prop(self, prop):
        '''
        Adds a prop to list, if the prop exists replace
        the existing props value
        '''
        # Checking if the prop exists
        current_prop = self.contains_prop(prop.get_name())
        # If Not Add a new Prop
        if(current_prop == None):
            self._props.append(prop)
        else:
            # Swaps the values
            current_prop.set_value(prop.get_value())

    def __str__(self):
        """
        Returns the block as a string
        with it's name and properties.
        """
        return "Block Name is " + self._name + " : " + str(self._props)

    def __repr__(self):
        '''
        Returns the block as a string
        with it's name and properties.
        '''
        return str(self)