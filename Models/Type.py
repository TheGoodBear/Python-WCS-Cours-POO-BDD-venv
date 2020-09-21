# coding: utf-8
import Variables as Var

class Type():
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
        self.id_parent = Properties[2]
        
        # calculated properties
        self.parent = None


    def get_parent(self):
        """
            Call the whosyourdaddy method
        """

        self.parent = self.whosyourdaddy(self.id_parent)

    def whosyourdaddy(self, parent_id, parent_list=[]):
        """
            Recursively find all the parents
        """

        # Get the current parent
        # TYPE              
        temp_parent = [type for type in Var.Types if parent_id == type.id]
        print(temp_parent)
        if temp_parent == []:
            return parent_list
        # add the parent to the list
        parent_list.append(temp_parent[0].name)
        print(parent_list)
        # Recall the method on the found parent using the ID
        self.whosyourdaddy(temp_parent[0].id_parent, parent_list)

    def __str__(self):
        """
            Overloads the print method
        """

        return f"({self.id}) {self.name} - {self.id_parent}"