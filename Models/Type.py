# coding: utf-8

# import additional code
import Models.GenericM as GM


class Type(GM.Model):
    """
        Model for Type table in database
    """

    # class properties
    TableName = "type"
    CollectionObject = "Types"
    ElementTitle = "le type d'animal"
    CollectionTitle = "types d'animaux"
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
            "Name" : "id_parent",
            "Label" : "IDParent",
            "Native" : True,
            "Key" : "type",
            "Add" : True,
            "Update" : True,
            "Print" : False
        },
        {
            "Name" : "parent_hierarchy",
            "Label" : "Hiérarchie",
            "Native" : False,
            "Key" : None,
            "Add" : False,
            "Update" : False,
            "Print" : True
        },
        {
            "Name" : "parent_name",
            "Label" : "Espèce",
            "Native" : False,
            "Key" : None,
            "Add" : False,
            "Update" : False,
            "Print" : False
        },
        {
            "Name" : "full_name",
            "Label" : "Espèce",
            "Native" : False,
            "Key" : None,
            "Add" : False,
            "Update" : False,
            "Print" : False
        },
    ]


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # inherits from parent constructor (native properties)
        super().__init__(Properties)
        
        # calculated properties
        self.parent_hierarchy = None    # full parent hierarchy as list
        self.parent_name = None         # printable parent hierarchy
        self.full_name = None           # name including hierarchy


    def GetParent(self, 
        MyCollection):
        """
            Call the WhosYourDaddy method
        """

        # get full hierarchy names list
        self.parent_hierarchy = self._WhosYourDaddy(self.id_parent, MyCollection)
        # reverse list (parent → children)
        self.parent_hierarchy.reverse()
        # format calculated properties string
        self.parent_name = " → ".join(self.parent_hierarchy)
        self.full_name = (
            " → ".join(self.parent_hierarchy + [self.name]) 
            if self.parent_hierarchy[0] != "Aucun" 
            else self.name)


    def _WhosYourDaddy(self, 
        parent_id, 
        MyCollection, 
        parent_list = None):
        """
            Recursively find all the parents
            and return a list of parents
            _ private methode
        """

        # init the empty list
        if parent_list is None:
            parent_list = []
        
        # if no parent
        if parent_id is None:
            return ["Aucun"]

        # Get the current parent type
        temp_parent = [
            type for type 
            in MyCollection 
            if parent_id == type.id]
        if temp_parent == []:
            return parent_list
        
        # add the parent to the list
        parent_list.append(temp_parent[0].name)
        # print(parent_list)
        
        # recall the method on the found parent using the ID
        self._WhosYourDaddy(temp_parent[0].id_parent, MyCollection, parent_list)
        
        # return result
        return parent_list


    def __str__(self):
        """
            Overloads the print method
        """

        return f"({self.id}) {self.name} - {self.parent_name}"