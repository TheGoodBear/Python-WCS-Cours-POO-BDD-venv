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
    ElementTitle = "l'animal"
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
    def Add(Model, FieldsValues):
        """
            Add new Model element in DB
            then refresh relative collection
            and return message confirmation
        """

        try:
            # get fields to add
            FieldsToAdd = [Field["Name"] for Field in Model.Fields if Field["Add"]]
            # create query
            SQLQuery = f"INSERT INTO {Model.TableName} "           
            SQLQuery += f"({', '.join(FieldsToAdd)}) "
            SQLQuery += "VALUES (%s, %s) "
            # add query parameters
            SQLValues = tuple(FieldsValues) 
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{Model.ElementTitle.capitalize()} a été ajouté."

        except Exception as Error:
            # error message
            return f"\n{Model.ElementTitle.capitalize()} n'a pas pû être ajouté dans la base de données.\n{Error}"

    
    @staticmethod
    def Update(Model, PKValue, FieldsValues):
        """
            Update Model element in DB with primary key value = PKValue
            then refresh relative collection
            and return message confirmation
        """

        try:
            # get fields to update
            FieldsToUpdate = [f"{Field['Name']} = %s" for Field in Model.Fields if Field["Update"]]
            # get primary key
            PrimaryKey = [Field["Name"] for Field in Model.Fields if Field["Key"] == "Primary"][0]
            # create query
            SQLQuery = f"UPDATE {Model.TableName} "
            SQLQuery += f"SET {', '.join(FieldsToUpdate)} "
            SQLQuery += f"WHERE {PrimaryKey} = %s"
            # add query parameters
            SQLValues = tuple(FieldsValues) + (PKValue, )
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} a été modifié."

        except Exception as Error:
            # error message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} n'a pas pû être modifié dans la base de données.\n{Error}"

    
    @staticmethod
    def Delete(Model, PKValue):
        """
            Delete Model element in DB with primary key value = PKValue
            then refresh relative collection
            and return message confirmation
        """

        try:
            # get primary key
            PrimaryKey = [Field["Name"] for Field in Model.Fields if Field["Key"] == "Primary"][0]
            # create query
            SQLQuery = f"DELETE FROM {Model.TableName} "
            SQLQuery += f"WHERE {PrimaryKey} = %s"
            # add query parameters
            SQLValues = (PKValue, )
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} a été supprimé."

        except Exception as Error:
            # error message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} n'a pas pû être supprimé dans la base de données.\n{Error}"

    
    def Delete2(self):
        """
            Delete Model element in DB with primary key value = PKValue
            then refresh relative collection
            and return message confirmation
        """

        PKValue = self.id
        try:
            # get primary key
            PrimaryKey = [Field["Name"] for Field in self.Fields if Field["Key"] == "Primary"][0]
            # create query
            SQLQuery = f"DELETE FROM {self.TableName} "
            SQLQuery += f"WHERE {PrimaryKey} = %s"
            # add query parameters
            SQLValues = (PKValue, )
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} a été supprimé."

        except Exception as Error:
            # error message
            return f"\n{Model.ElementTitle.capitalize()} numéro {PKValue} n'a pas pû être supprimé dans la base de données.\n{Error}"
