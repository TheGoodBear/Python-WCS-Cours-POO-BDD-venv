# coding: utf-8

# import additional code
import Variables as Var
import Models.GenericM as GM


class Animal(GM.Model):
    """
        Model for Animal table in database
    """

    # class properties
    TableName = "animal"
    CollectionObject = "Animals"
    ElementTitle = "l'animal"
    CollectionTitle = "animaux"
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
        {
            "Name" : "id_type",
            "Label" : "IDType",
            "Native" : True,
            "Key" : "type",
            "Add" : True,
            "Update" : True,
            "Print" : False
        },
        {
            "Name" : "type",
            "Label" : "Espèce",
            "Native" : False,
            "Key" : None,
            "Add" : False,
            "Update" : False,
            "Print" : False
        },
        {
            "Name" : "full_type",
            "Label" : "Espèce",
            "Native" : False,
            "Key" : None,
            "Add" : False,
            "Update" : False,
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

        # inherits from parent constructor (native properties)
        super().__init__(Properties)
        
        # calculated properties
        self.type = self.GetTypeName()              # type name matching id_type
        self.full_type = self.GetTypeName(True)     # full type name (with all hierarchy) matching id_type


    def __str__(self):
        """
            Overloads the print method
        """

        return f"({self.id}) {self.name} - {self.full_type} ({self.id_type})"


    def GetTypeName(self,
        GetHierarchy = False):
        """
            Get type name (or full name with parent hierarchy) from id
        """
        
        if GetHierarchy:
            # return full type name (with hierarchy)
            return [
                MyType.full_name
                for MyType
                in Var.Types
                if MyType.id == self.id_type][0]
        else:
            # return only type name
            return [
                MyType.name
                for MyType
                in Var.Types
                if MyType.id == self.id_type][0]
