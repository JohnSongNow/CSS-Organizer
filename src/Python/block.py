class Block():
    """
    A single CSS Block in CSS-Organizer, contains the name and type of block
    that it is as well as contains a list of all CSS properties in the block. By default
    the block does not check if the props within the CSS is valid and must be explicatly
    called.
    """
    
    def __init__(self, name, props=[]):
        self._props = props
        self._name = name
    
    
    def changeName(self, name):
        self._name = name
    
    
    def changeProps(self, props):
        self._props = props
        
        
    def removePropByName(self, name):
        '''
        Removes the property within the list
        '''
        # Gets ths removed propr, None if not present
        removed_prop = self.containsProperty(name)
        
        # Removing the prop
        if(removed_prop == None):
            return
        self._props.remove(removed_prop)
            
        
    def containsProperty(self, name):
        """
        Checks if the block contains the property with
        the following name. If it does return the property
        """
        # New list of only the property with the wanted name
        new_list = [x for x in self._props if x.getName() == name]
        
        # If nothing fits the description
        if(len(new_list) == 0):
            return None
        # Returns the first element
        return new_list[0]
    
    
    def addProp(self, prop):
        '''
        Adds a prop to list, if the prop exists replace
        the existing props value
        '''
        # Checking if the prop exists
        current_prop = self.containsProperty(prop.getName())
        # If Not Add a new Prop
        if(current_prop == None):
            self._props.append(prop)
        else:
            # Swaps the values
            current_prop.setValue(prop.getValue())

    
    def __str__(self):
        """
        Returns the block as a string
        with it's name and properties.
        """
        return "Block Name is : " + self._name + " : " + str(self._props)