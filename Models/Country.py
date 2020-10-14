# coding: utf-8

# import additional code
import Variables as Var
import Models.GenericM as GM


class Country(GM.Model):
    """
        Model for Country table in database
    """

    # class properties
    TableName = "country"
    CollectionObject = "Countries"
    ElementTitle = "le pays"
    CollectionTitle = "pays"
    Fields = [
        {
            "Name" : "id",
            "Label" : "ID",
            "Native" : True,
            "Key" : "Primary",
            "Add" : False,
            "Update" : False,
            "Print" : True
        },
        {
            "Name" : "name",
            "Label" : "Nom",
            "Native" : True,
            "Key" : None,
            "Add" : True,
            "Update" : True,
            "Print" : True
        },
    ]


    # methods
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
