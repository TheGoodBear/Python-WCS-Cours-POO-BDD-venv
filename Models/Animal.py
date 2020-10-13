# coding: utf-8

# import additional code
import Variables as Var
import Utilities.DBUtil as DB
import Utilities.ApplicationUtilities as App
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


    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # inherits from parent constructor
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

    
    # @staticmethod
    # def GetInstance(ID):
    #     """
    #         Get Animal with specified ID from collection
    #     """

    #     # get from collection
    #     AnimalList = [
    #         Animal 
    #         for Animal 
    #         in Var.Animals 
    #         if Animal.id == ID]
        
    #     # return animal object if found else None
    #     return AnimalList[0] if len(AnimalList) == 1 else None

    
    # @staticmethod
    # def Add(Name, IDType):
    #     """
    #         Add MyAnimal in DB,
    #         refresh collection
    #         and return message confirmation
    #     """

    #     try:
    #         # add data in DB
    #         SQLQuery = f"INSERT INTO {Animal.TableName} "
    #         SQLQuery += "(name, id_type) "
    #         SQLQuery += "VALUES (%s, %s) "
    #         SQLValues = (Name, IDType)
    #         DB.ExecuteQuery(SQLQuery, SQLValues, True)

    #         # refresh collections from DB
    #         App.InitializeData()
            
    #         # success message
    #         return f"\nL'animal a été ajouté."

        # except:
        #     # error
        #     return f"\nL'animal n'a pas pû être ajouté dans la base de données."

    
    # @staticmethod
    # def Edit(MyAnimal):
    #     """
    #         Update MyAnimal in DB,
    #         refresh collection
    #         and return message confirmation
    #     """

    #     try:
    #         # update data in DB
    #         SQLQuery = f"UPDATE {Animal.TableName} "
    #         SQLQuery += "SET name = %s, id_type = %s "
    #         SQLQuery += "WHERE id = %s"
    #         SQLValues = (MyAnimal.name, MyAnimal.id_type, MyAnimal.id)
    #         DB.ExecuteQuery(SQLQuery, SQLValues, True)

    #         # refresh collections from DB
    #         App.InitializeData()
            
    #         # success message
    #         return f"\nL'animal numéro {MyAnimal.id} a été modifié."

    #     except:
    #         # error
    #         return f"\nL'animal numéro {MyAnimal.id} n'a pas pû être modifié dans la base de données."

    
    # @staticmethod
    # def Delete(ID):
    #     """
    #         Delete Animal with specified ID from DB,
    #         refresh collection
    #         and return message confirmation
    #     """

    #     try:
    #         # delete data in DB
    #         SQLQuery = f"DELETE FROM {Animal.TableName} "
    #         SQLQuery += "WHERE id = %s"
    #         SQLValues = (ID, )
    #         DB.ExecuteQuery(SQLQuery, SQLValues, True)

    #         # refresh collections from DB
    #         App.InitializeData()
            
    #         # success message
    #         return f"\nL'animal numéro {ID} a été supprimé."

    #     except:
    #         # error
    #         return f"\nL'animal numéro {ID} n'a pas pû être supprimé dans la base de données."

    
    @classmethod
    def GetData(cls, ID):
        """
            Get animal with specified ID from collection
            And return animal object and data in list if not None 
            else return None and not exist message
        """

        # get animal from collection
        MyAnimal = cls.GetInstance(Animal, ID)

        if MyAnimal is not None:
            return (MyAnimal, 
                [f"\nID → {MyAnimal.id}",
                f"Nom → {MyAnimal.name}",
                f"Type → {MyAnimal.type}"])
        else:
            return (None, [f"\nL'animal numéro {ID} n'existe pas."])
