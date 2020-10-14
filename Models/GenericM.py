# coding: utf-8

# import modules
from enum import Enum

# import additional code
import Variables as Var
import Utilities.DBUtil as DB
import Utilities.ApplicationUtilities as App

# enumerations
class eFiledTypes(Enum):
    PrimaryKey = 0
    Add = 1
    Update = 2
    Print = 3


class Model():
    """
        Generic class for Models
    """

    # class properties
    TableName = ""
    CollectionObject = ""
    ElementTitle = "l'animal"
    CollectionTitle = ""


    # methods    
    def __init__(self,
        Properties):
        """
            Constructor
            Instance properties
        """

        # native properties
        for index, Field in enumerate(self.Fields):
            if Field["Native"]:
                setattr(self, Field["Name"], Properties[index])
        
    
    def _GetFields(self, 
        FieldType = eFiledTypes.PrimaryKey):
        """
            Get fields names and values of current Model instance
            matching field type
        """

        if FieldType == eFiledTypes.PrimaryKey:
            # get primary key name
            PrimaryKeyName = [Field["Name"] for Field in self.Fields if Field["Key"] == "Primary"][0]
            # get primary key value
            PrimaryKeyValue = getattr(self, PrimaryKeyName)
            # return data
            return PrimaryKeyName, PrimaryKeyValue
        elif FieldType == eFiledTypes.Print:
            # for print action
            # get fields names and labels
            FieldsData = [(Field["Name"], Field["Label"]) for Field in self.Fields if Field[FieldType.name]]
            FieldsValues = []
            for FieldData in FieldsData:
                # get field value for each field
                FieldsValues.append(getattr(self, FieldData[0]))
            # return fields labels and values
            return [FieldData[1] for FieldData in FieldsData], tuple(FieldsValues)
        else:
            # for specified CRUD action (Add, Update)
            # define field name suffix
            FieldNameSuffix = " = %s" if FieldType == eFiledTypes.Update else ""
            # get fields names
            FieldsNames = [Field["Name"] for Field in self.Fields if Field[FieldType.name]]
            # get fields values and format field name for each field
            FieldsValues = []
            FormattedFieldsNames = []
            for FieldName in FieldsNames:
                FieldsValues.append(getattr(self, FieldName))
                FormattedFieldsNames.append(f"{FieldName}{FieldNameSuffix}")
            # return data
            return FormattedFieldsNames, tuple(FieldsValues)
        
    
    # methods    
    @classmethod
    def GetInstance(cls, ID):
        """
            Get Element with specified ID
            from Model collection
        """

        # get from collection
        Elements = [
            Element 
            for Element 
            in eval(f"Var.{cls.CollectionObject}") 
            if Element.id == ID]
        
        # return instance if found else None
        return Elements[0] if len(Elements) == 1 else None


    @classmethod
    def GetData(cls, ID):
        """
            Get instance data of Model from collection
            And return the instance object and data in list if not None 
            else return None and not exist message
        """

        # get instance from collection
        MyInstance = cls.GetInstance(ID)

        if MyInstance is not None:
            # get fields to print
            FieldsNames, FieldsValues = MyInstance._GetFields(eFiledTypes.Print)
            PrintResults = [""]
            for FieldIndex in range(len(FieldsNames)):
                # for each field, format string to print with name and value
                PrintResults.append(f"{FieldsNames[FieldIndex]} : {FieldsValues[FieldIndex]}")
            # return list of strings
            return MyInstance, PrintResults
            
        else:
            return (None, [f"\n{cls.ElementTitle.capitalize()} numéro {ID} n'existe pas."])

    
    def Add(self):
        """
            Add new instance of Model in DB
            then refresh relative collection
            and return message confirmation
        """
        
        # get fields to add
        FieldsNames, FieldsValues = self._GetFields(eFiledTypes.Add)
        # create values placeholders in query (%s) for each field
        FieldsValuesPlaceHolders = ", ".join(["%s"] * len(FieldsValues))

        try:
            # create query
            SQLQuery = f"INSERT INTO {self.TableName} "           
            SQLQuery += f"({', '.join(FieldsNames)}) "
            SQLQuery += f"VALUES ({FieldsValuesPlaceHolders}) "
            # add query parameters
            SQLValues = tuple(FieldsValues) 
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{self.ElementTitle.capitalize()} a été ajouté."

        except Exception as Error:
            # error message
            return f"\n{self.ElementTitle.capitalize()} n'a pas pû être ajouté dans la base de données.\n{Error}"

    
    def Update(self):
        """
            Update current instance of Model in DB
            then refresh relative collection
            and return message confirmation
        """

        # get primary key name and value
        PrimaryKeyName, PrimaryKeyValue = self._GetFields()
        # get fields to update
        FieldsNames, FieldsValues = self._GetFields(eFiledTypes.Update)

        try:
            # create query
            SQLQuery = f"UPDATE {self.TableName} "
            SQLQuery += f"SET {', '.join(FieldsNames)} "
            SQLQuery += f"WHERE {PrimaryKeyName} = %s"
            # add query parameters
            SQLValues = tuple(FieldsValues) + (PrimaryKeyValue, )
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{self.ElementTitle.capitalize()} numéro {PrimaryKeyValue} a été modifié."

        except Exception as Error:
            # error message
            return f"\n{self.ElementTitle.capitalize()} numéro {PrimaryKeyValue} n'a pas pû être modifié dans la base de données.\n{Error}"
    
    
    def Delete(self):
        """
            Delete current instance of Model in DB
            then refresh relative collection
            and return message confirmation
        """

        # get primary key name and value
        PrimaryKeyName, PrimaryKeyValue = self._GetFields()

        try:
            # create query
            SQLQuery = f"DELETE FROM {self.TableName} "
            SQLQuery += f"WHERE {PrimaryKeyName} = %s"
            # add query parameters as tuple
            SQLValues = (PrimaryKeyValue, )
            # execute query
            DB.ExecuteQuery(SQLQuery, SQLValues, True)

            # refresh collections from DB
            App.InitializeData()
            
            # success message
            return f"\n{self.ElementTitle.capitalize()} numéro {PrimaryKeyValue} a été supprimé."

        except Exception as Error:
            # error message
            return f"\n{self.ElementTitle.capitalize()} numéro {PrimaryKeyValue} n'a pas pû être supprimé dans la base de données.\n{Error}"
