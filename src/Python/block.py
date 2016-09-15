class Block():
    """
    A single CSS Block in CSS-Organizer, contains the name and type of block
    that it is as well as contains a list of all CSS properties in the block.
    By default the block does not check if the props within the CSS is valid
    and must be explicatly called.
    """

    def __init__(self, names, props):
        self._names = names.split(' ')
        self._props = props

    def set_names(self, names):
        self._names = names

    def get_names(self):
        '''
        Returns a list with the names of the block
        in order
        '''
        return self._names

    def set_props(self, props):
        self._props = props

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

    def organize(self, options, order):
        '''
        Organizes the block by organizing the props within.
        Takes in an option dict and orders them.
        '''
        for prop in self._props:
            prop.organize()

        new_prop_list = []

        # Replace with a lamba statement later
        for key in order["order"]:
            for value in order[key]:
                for prop in self._props:
                    if(value == prop.get_name()):
                        new_prop_list.append(prop)

                        print(str(new_prop_list))
                        break

        self._props = new_prop_list


    def __str__(self):
        """
        Returns the block as a string
        with it's name and properties.
        """
        return "Block Name is " + str(self._names) + " : " + str(self._props)

    def __repr__(self):
        '''
        Returns the block as a string
        with it's name and properties.
        '''
        return str(self)