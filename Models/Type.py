# coding: utf-8

import Models.GenericM as GM
import Variables as Var

class Type(GM.Model):
    """
        Model for Type table in database
    """

    # class properties
    TableName = "type"
    CollectionObject = "Types"
    CollectionTitle = "types d'animaux"


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # native properties
        self.id = Properties[0]
        self.name = Properties[1]
        self.id_parent = Properties[2]
        
        # calculated properties
        self.parent_hierarchy = None    # full parent hierarchy as list
        self.parent_name = None         # printable parent hierarchy
        self.full_name = None           # name including hierarchy


    def GetParent(self, MyCollection):
        """
            Call the WhosYourDaddy method
        """

        self.parent_hierarchy = self._WhosYourDaddy(self.id_parent, MyCollection)
        self.parent_name = ' → '.join(self.parent_hierarchy)
        self.full_name = ' → '.join(self.parent_hierarchy + [self.name])


    def _WhosYourDaddy(self, parent_id, MyCollection, parent_list=None):
        """
            Recursively find all the parents
            and return a list of parents
            _ private methode
        """

        # Init the empty list
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
        
        # Recall the method on the found parent using the ID
        self._WhosYourDaddy(temp_parent[0].id_parent, MyCollection, parent_list)
        
        # return result
        return parent_list


    def __str__(self):
        """
            Overloads the print method
        """

        return f"({self.id}) {self.name} - {self.parent_name}"