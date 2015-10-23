from block import *


class Property():
    """
    A single property in CSS-Organizer, contains the name and the value
    of the CSS property that it holds. Note that the property by default is
    not checked to be valid and must be explictly called.

    Attributes:
        _type: The type of the property
        _ name: The name of the property
        _value: The value of the property
    """

    def __init__(self, name, value, type="Misc"):
        self.changeProperty(name, value)
        self._type = type

    def getName(self):
        return self._name

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def changeProperty(self, name, value):
        """
        Changes the property of the
        """
        self._name = name
        self._value = value
        self.changeType()

    def isValid(self):
        """
        Checks if the current value for the property
        is valid, iff the property is valid.
        """

    def changeType(self):
        """
        Changes the type of the current property, by
        default thr type of property is Misc.
        """
        # Switching between the different types of properties
        if(self._name == "Test"):
            self._type = "Test"
        elif(False):
            self._type = "Position"
            self._type = "Display"
            self._type = "Font"
            self._type = "Colour"
            self._type = "Animation"
        else:
            self._type = "Misc"

    def getType(self):
        return

    def __str__(self):
        """
        Returns the a str representing the property
        with it's name and value respentively.
        """
        return '[' + str(self._name) + ', ' + str(self._value) + ']'

    def __repr__(self):
        """
        Returns the a str represnetion of the property
        with it's name and value respentively
        """
        return str(self)
