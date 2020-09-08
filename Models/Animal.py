# coding: utf-8

import Variables as Var

class Animal():
    """
        Model for Animal table in database
    """

    def __init__(self,
        ID, Name, IDType):
        """
            Constructor
        """

        # native properties
        self.id = ID
        self.name = Name
        self.id_type = IDType
        
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
        self.type = [
            MyType.name
            for MyType
            in Var.Types
            if MyType.id == self.id_type][0]