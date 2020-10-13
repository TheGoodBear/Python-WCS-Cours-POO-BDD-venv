# coding: utf-8

import Models.GenericM as GM

class Country(GM.Model):
    """
        Model for Type table in database
    """

    # class properties
    TableName = "country"
    CollectionObject = "Countries"
    ElementTitle = "le pays"
    CollectionTitle = "pays"


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """
        
        # native properties
        self.id = Properties[0]
        self.name = Properties[1]


    def __str__(self):
        """
            Overloads the print method
        """
        return f"({self.id}) {self.name}"
