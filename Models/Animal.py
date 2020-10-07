# coding: utf-8

import Variables as Var
import Models.GenericM as GM

class Animal(GM.Model):
    """
        Model for Animal table in database
    """

    # class properties
    TableName = "animal"
    CollectionObject = "Animals"
    CollectionTitle = "animaux"


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # native properties
        self.id = Properties[0]
        self.name = Properties[1]
        self.id_type = Properties[2]
        
        # calculated properties
        # MyQuery = (
        #     "SELECT type.name " +
        #     "FROM type " + 
        #     f"WHERE type.id = {self.id_type}")
        # MyResult = ExecuteQuery(MyConnection, MyQuery)
        # self.type = ""
        # for MyType in Var.Types:
        #     if MyType.id == self.id_type:
        #         self.type = MyType.name 
        self.type = self.GetTypeName()
        self.full_type = self.GetTypeName()


    def __str__(self):
        """
            Overloads the print method
        """

        return f"({self.id}) {self.name} - {self.type} ({self.id_type})"


    def GetTypeName(self,
        GetHierarchy = False):
        """
            Get type name (or full name with parent hierarchy) from id
        """
        
        if GetHierarchy:
            return [
                MyType.full_name
                for MyType
                in Var.Types
                if MyType.id == self.id_type][0]
        else:
            return [
                MyType.name
                for MyType
                in Var.Types
                if MyType.id == self.id_type][0]
