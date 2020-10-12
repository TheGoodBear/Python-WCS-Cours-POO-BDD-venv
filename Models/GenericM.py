# coding: utf-8

# import additional code
import Variables as Var
import Utilities.DBUtil as DB
import Utilities.ApplicationUtilities as App

class Model():
    """
        Generic class for Models
    """

    # class properties
    TableName = ""
    CollectionObject = ""
    CollectionTitle = ""


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # native properties
        for index, Field in enumerate(self.Fields):
            if Field["Native"]:
                setattr(self, Field['Name'], Properties[index])
        
    
    # methods    
    @staticmethod
    def GetInstance(Model, ID):
        """
            Get Element with specified ID
            from Model collection
        """

        # get from collection
        Elements = [
            Element 
            for Element 
            in eval(f"Var.{Model.CollectionObject}") 
            if Element.id == ID]
        
        # return instance if found else None
        return Elements[0] if len(Elements) == 1 else None

    
    @staticmethod
    def Add(Model, *args):
        """
            Add new model element in DB,
            refresh relative collection
            and return message confirmation
        """

        print("add")

        try:
            # add data in DB
            SQLQuery = f"INSERT INTO {Model.TableName} "
            
            SQLQuery += "(name, id_type) "
            SQLQuery += "VALUES (%s, %s) "
            SQLValues = *args
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\nL'animal a été ajouté."

        except:
            # error
            return f"\nL'animal n'a pas pû être ajouté dans la base de données."
