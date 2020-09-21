# coding: utf-8

from os import name


class Country():
    """
        Model for Type table in database
    """

    def __init__(self,
        Properties):
        """
            Constructor
        """
        
        # native properties
        self.id = Properties[0]
        self.name = Properties[1]

    def __str__(self):
        """
            Overloads the print method
        """
        return f"({self.id}) {self.name}"
