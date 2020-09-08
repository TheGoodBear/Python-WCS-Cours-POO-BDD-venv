# coding: utf-8

class Type():
    """
        Model for Type table in database
    """

    def __init__(self,
        ID, Name, IDParent):
        """
            Constructor
        """

        # native properties
        self.id = ID
        self.name = Name
        self.id_parent = IDParent
        
        # calculated properties
        # self.Parent = ""